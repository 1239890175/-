
import os
import time
import requests
from mspiderx import sx
import threading
import pandas as pd



class 报价监控:
    def __init__(self) -> None:
        # 报价接口key

        # 设置报价文件目录
        # 正在读取后端文件
        print('正在读取后端文件')
        self.folder_path='./报价数据/'
        self.pz_data=sx.加载配置文件({})
        self.cookie_file='cookie.txt'
        print(self.pz_data.get('后端大表','库存&成本-后台产品库(5).csv'))
        self.bd_data=pd.read_csv(self.pz_data.get('后端大表','库存&成本-后台产品库(5).csv'))
        if '报价日期' not in self.bd_data.columns.to_list():
            self.bd_data['报价日期']=''
        print('读取完毕')
        

    # 下载表格
    def get_bg_xlsx(self):
        try:
            os.mkdir( self.folder_path)
        except:
            pass
        while True:
            now_date=sx.时间戳转日期格式(time.time(),中文=True).split(' ')[0]
            try:
                os.mkdir(self.folder_path+now_date)
            except:
                pass

            header_t=f'''Host: zc.plap.mil.cn
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0
        Cookie:{open(self.cookie_file,'r',encoding='utf-8').read()}  '''
        #     "VerifyCode": "sj39Y9ZEkx4^%^3D",

            headers = sx.dict_From_HeadersStr(header_t)
            while 1:
                url = "https://zc.plap.mil.cn/EpointMallService/rest/product_producttemp/canExcel"
                data = {
                    "frameBodySecretParam": "JTdCJTIydHlwZSUyMiUzQSUyMjExMSUyMiUyQyUyMnJlZmVyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnpjLnBsYXAubWlsLmNuJTJGbG9jYWxwcmljZS5odG1sJTIyJTdE"
                }
                # data={ 'type': "111", 'referer': "https://zc.plap.mil.cn/localprice.html" }
                response = requests.post(url, headers=headers, data=data)
                # #print(response.json())
                try:
                    url = "https://zc.plap.mil.cn/EpointMallService/rest/product_producttemp/exportBJProduct"
                    data = {
                        "frameBodySecretParam": "JTdCJTIyY2lkJTIyJTNBJTIyJTIyJTJDJTIyeGRwcm9kdWN0Y29kZSUyMiUzQSUyMiUyMiUyQyUyMnByb2R1Y3RuYW1lJTIyJTNBJTIyJTIyJTJDJTIyc2t1JTIyJTNBJTIyJTIyJTJDJTIyYnJhbmRuYW1lJTIyJTNBJTIyJTIyJTJDJTIyc3RhdHVzJTIyJTNBJTIyMCUyMiUyQyUyMmlzdHVpamlhbiUyMiUzQSUyMiUyMiUyQyUyMnJlZmVyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnpjLnBsYXAubWlsLmNuJTJGbG9jYWxwcmljZS5odG1sJTIyJTdE\u0000"
                    }
                    response = requests.post(url, headers=headers, data=data,timeout=10)
                except:
                    pass
                t=0
                if '上次导出未完成，请勿频繁导出' in response.text:
                    break
                else:
                    time.sleep(5)
            while 1:
                url = "https://zc.plap.mil.cn/EpointMallService/rest/product_producttemp/getExcelList"
                data = {
                    "frameBodySecretParam": "JTdCJTIydHlwZSUyMiUzQSUyMjExJTIyJTJDJTIycGFnZSUyMiUzQTElMkMlMjJzaXplJTIyJTNBMTAlMkMlMjJyZWZlcmVyJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZ6Yy5wbGFwLm1pbC5jbiUyRmV4cG9ydGhpc3RvcnkuaHRtbCUzRnR5cGUlM0QxMSUyMiU3RA%3D%3D"
                }
                response = requests.post(url, headers=headers, data=data)
                res_json=response.json()
                # #print(res_json)
                file = res_json['userarea']['fileList'][0]
                if t==0:
                    t=file['times'] 
                    # #print('等待')
                    time.sleep(20)
                    continue
                # #print(file['times'] , t)
                if file['times'] > t:
                    # #print("获取到最新文件")
                    file_url = file['url']
                    file_name = file['filename']
                    # #print(file_url)
                    # #print(file_name)
                    response = requests.get(file_url, headers=headers)
                    #print(response)
                    #print(response.headers)
                    if int(response.headers['Content-Length'])<5796807:
                        time.sleep(20)
                        continue
                    with open(self.folder_path+now_date+'/'+file_name, 'wb') as f:
                        f.write(response.content)
                        f.close()
                    break
                else:
                    # #print('等待')
                    time.sleep(20)
                    continue
            time.sleep(int(self.pz_data.get('监控间隔','60')))
    
    def get_new_file_path(self):
        now_date=sx.时间戳转日期格式(time.time(),中文=True).split(' ')[0]
        folder_path= self.folder_path+now_date
        latest_files = {}
        for filename in os.listdir(folder_path):
            full_path = os.path.join(folder_path, filename)
            if os.path.isfile(full_path):
                modification_time = os.path.getmtime(full_path)
                latest_files[filename] = modification_time

        latest_file_name = max(latest_files, key=latest_files.get)

        latest_file_full_path = os.path.join(folder_path, latest_file_name)
        return latest_file_full_path
    
    def set_price(self):
          while 1:
            try:
                self.bj_data=pd.read_excel(self.get_new_file_path())
                self.bj_data[self.bj_data['最低价']=='暂无报价']=999999999
                now_t=int(sx.时间戳转日期格式(time.time(),中文=True).split(' ')[-1].split('分')[0].replace('时',''))
                for file_name in os.listdir('设置'):
                    # 到了文件设定的时间后
                    t=int(file_name.split('.')[0].replace('_',''))
                    if t < now_t:
                        #print('开始改价')
                        # 读取需要改价格的编码
                        set_data=pd.read_csv('设置/'+file_name,names=['商品编码'])
                        # 从报价表格中筛选需要改价的商品
                        df=self.bj_data[self.bj_data['商品编码'].isin(set_data['商品编码'])]
                        # 合并下大表数据
                        merged_df = pd.merge(self.bd_data, df, how='left', left_on='军采编码',right_on='商品编码')
                        filtered_df = merged_df[merged_df['商品名称'].notnull()]  # 或者使用 .dropna(subset=['value'])
                        # 筛选一下不是锁定状态 并且当前报价小于本地报价时 没有报价的
                        df2=filtered_df[(self.bd_data['锁定状态(1是锁定2是不锁定)']==2) & (filtered_df['报价'].astype(float)!=filtered_df['最低价_y'].astype(float)) & ((filtered_df['最低价_y'].astype(float)-float(self.pz_data.get('降价步长','0.1')))>(filtered_df['厂家成本'].astype(float)*(1+(float(self.pz_data.get('限制利润率','10'))/100)))) & (filtered_df['报价日期'] != sx.时间戳转日期格式(time.time(),中文=True).split(' ')[0])]
                        # df2=bd_data[(bd_data['军采编码'].isin(df['商品编码'])) & (bd_data['锁定状态(1是锁定2是不锁定)']==2) & (bd_data['报价']>df['最低价'])]
                 
                        self.bd_data.loc[df2.index,'报价']=df2['最低价_y'].astype(float)-float(self.pz_data.get('降价步长','0.1'))
                       
                        self.bd_data.loc[df2.index,'报价日期']=sx.时间戳转日期格式(time.time(),中文=True).split(' ')[0]
                                    
                        column_rename_mapping = {
    '编码': 'goods_sku',
    '报价': 'bottom_price',
    # ... 其他列名替换规则
}                       
                        df_renamed =self.bd_data.loc[df2.index][['编码','报价']].rename(columns=column_rename_mapping)
                        print(file_name)
                        if not df_renamed.empty:
                            print('符合改价')
                            print(df_renamed)
                            self.putTlj(df_renamed.to_dict('records'))
                            print('改价完成')
                        self.bd_data.to_csv(self.pz_data.get('后端大表','库存&成本-后台产品库(5).csv'),index=False)
                     
                #print(self.get_new_file_path())
            except Exception as e:
                pass
                #print(e)
            time.sleep(10)
    def run(self):

        thread=threading.Thread(target=self.get_bg_xlsx, args=())
        thread.start()
      
    
    def putTlj(self,d):
        
        url = self.pz_data.get('同步最低价接口','http://47.111.126.189:999/jun/TljApis/syncBottomPrice')
        data={
"appkey": self.pz_data.get('appkey','10000011'),
"appsecret": self.pz_data.get('appsecret','bbbbbbbb'),
"goods":d
}

        res=sx.post_request(url=url,json_=data)
        print(res.json())

if __name__ == '__main__':
    print('开始监控')
    jk=报价监控()
    jk.run()




# 开始改价
#                                goods_sku  bottom_price
# 2   e61bc8a7-5acc-43a4-b501-3132cd12d9bc        734.60
# 6   f5f33afa-f93a-46e9-8e88-af4baba7266e        278.97
# 7   2282f3a7-ff64-497f-895f-2f884e54fe09        141.46
# 8   c5ab71cc-eeee-4e26-b7b2-34c61db01933        942.59
# 10  691adeaf-6d00-4a44-b7e6-42bc678cb1a8        139.28
# 13  7b0ec533-2071-4018-9497-d049fe135df8        174.46
# 14  c4f78d07-a2a4-4994-8576-b0f7e0bdadf3        223.89  =======
# 15  ba519888-1a46-4966-9e24-0a40406d6d16        134.80
# 16  28c4f624-cdc3-4a3b-8d49-d796bd2359cc        237.86
# 17  358f5ccc-b2c6-439b-a55a-143da99c8437       5559.30
# 18  6f2ac934-879e-497c-b632-b15249940890        656.70
# 20  ff378770-b6b0-4e86-83ba-4bd7ae34a9d9        164.89
# 22  962bdc5e-a855-4bf2-9ecd-ed2470a771cb       9866.84
# 23  1c625524-3d6d-4bb5-81bd-073570636aae        176.25
# 24  fc9bc30d-3a4d-4a65-9345-97af8ccfe7a3       1585.90
# 27  83963862-26eb-402e-b4ff-01bee44fc8d3       1878.90
# 34  363346fd-16ba-4f7a-bcff-30931f51314c       1067.80
# 36  a8d6837a-dd80-410f-baa4-18200ba46a2c      20494.29
# 37  1759fb9a-1cd8-43da-93ac-aa0d4cf820cf       2755.10
# 38  45adeeb1-c052-4b2d-a81c-b9a3ad859005       7493.10
# {'data': {'msg': '同步成功'}, 'returnMsg': 'success', 'isSuccess': True, 'log_id': '82071'}