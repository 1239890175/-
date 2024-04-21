
# 报价数据统计类
import os
import pandas as pd
import warnings

# 忽略所有警告
warnings.filterwarnings("ignore")

# 或者只忽略特定类型的警告，例如 DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# 然后进行您的其他代码操作...
class BJDataStatistics:
    def __init__(self) -> None:
        self.folder_path='./报价数据/'
        # 定义个方法获取folder_path目录下的所有目录
        self.folder_list=[]
        for folder in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path,folder)):
                self.folder_list.append(os.path.join(self.folder_path,folder))
        self.folder_list.sort(reverse=True)
        # folder_list 排序降序       
    def folder_table_data_statistics(self, folder: str):
        """
        统计指定文件夹中所有Excel表格的数据

        参数:
        folder (str): 需要统计表格数据的文件夹路径。

        输出:
        通过 `print` 函数实时输出读取进度和统计结果。

        """
        df_list = []
        total_files = len([f for f in os.listdir(folder) if f.endswith('.xlsx')])
        current_file = 1

        for file in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, file)):
                if file.endswith('.xlsx'):
                    print(f"正在读取文件 {current_file}/{total_files}: {file}")
                    try:
                        df_list.append(pd.read_excel(os.path.join(folder, file)))
                    except Exception as e:
                        print(f"读取文件 {file} 时出错: {e}")
                    current_file += 1

        df = pd.concat(df_list)
        print("\n数据读取完成，合并后的数据框如下：")
        print(df)
        
        
    #  定义个方法用于选择需要统计的文件夹传入folder_table_data_statistics方法
    def select_folder(self):
        """
        选择需要统计的文件夹
        """
        while True:
            print("-----------------------------")
            print("请选择需要统计的文件夹:")
            for i, folder in enumerate(self.folder_list):
                print(f"{i+1}. {folder}")
            choice = input("请输入文件夹序号: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.folder_list):
                    self.folder_table_data_statistics(self.folder_list[choice-1])
                    # return self.folder_list[choice-1]
            except ValueError:
                print("无效的输入，请输入数字。")
        


if __name__ == '__main__':
    BJDS=BJDataStatistics()
    print(BJDS.folder_list)
    BJDS.folder_table_data_statistics(BJDS.folder_list[0])


