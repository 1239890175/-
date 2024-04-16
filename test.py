import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://zc.plap.mil.cn/localprice.html",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://zc.plap.mil.cn",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
cookies = {
    "VerifyCode": "sj39Y9ZEkx4%3D",
    "ispop": "1",
    "userinfo": "2goZRGBgWMII02xcTkAtXJfXXct6JcXFIfQ%2BR%2FLdqDYcYNvENUfsas6cl58dq25HRDyQUX%2BUra9I%0AnYTFP4stJzaQ0xd7wNHVfQi7oR8hensoxQ9BxyRa1RViTpjZb0NFHtdqYvuRKM%2BwccE%2BHmxa%2FyTQ%0AlS3bx6sIos0NcyFJHMs8DdRt%2FhMzrmFdYefkdk2vga7Llr53z6ZvG4O4O%2BPNYBoTPcPHDYEKKPCR%0AnLI0kG7KyhIDMY8v6nIq1X1KwuGF6EWPLqtKQWy%2F3yzTZRih%2BiGbxG0PJpxw7VYFmtJufRfCVUwD%0A6fjBe3c6fTk1m5ekKP%2BzMZtRl16L7I9rfkGU8igRnCPz1b3C7yqCFMmrJn3xbcdX6UWaHkizsXfk%0AxQ8B%2BQyRWPX9jwXM0JHGAz8%2FpyPqv6kfmbfODzV6EehAUV%2F%2BqXF%2FlG3u81no%2FkwcsJf6%2F%2FO9osxJ%0ACIH2Yj2rcRWQXo7lMfrMCpetWwYLR2kZLtWYjR903kaeZPL5N5heOkgTc%2FzEZUxaAGgnQNTqSk4Q%0A0j55CtwmMXh9bThKr6x6NctDrrOMT6CxGB3I%2FlKlMLLp%0A",
    "gysgroup": "1%3B3%3B",
    "usertype": "2",
    "displayname": "%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B3%B0%E9%BE%99%E5%90%89%E8%B4%B8%E6%98%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8",
    "nickname": "%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B3%B0%E9%BE%99%E5%90%89%E8%B4%B8%E6%98%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8",
    "danweiname": "%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B3%B0%E9%BE%99%E5%90%89%E8%B4%B8%E6%98%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8",
    "ismain": "1",
    "permission": "\"\""
}
url = "https://zc.plap.mil.cn/EpointMallService/rest/product_producttemp/canExcel"
data = {
    "frameBodySecretParam": "JTdCJTIydHlwZSUyMiUzQSUyMjExMSUyMiUyQyUyMnJlZmVyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnpjLnBsYXAubWlsLmNuJTJGbG9jYWxwcmljZS5odG1sJTIyJTdE\u0000"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)

url = "https://zc.plap.mil.cn/EpointMallService/rest/product_producttemp/exportBJProduct"
data = {
    "frameBodySecretParam": "JTdCJTIyY2lkJTIyJTNBJTIyJTIyJTJDJTIyeGRwcm9kdWN0Y29kZSUyMiUzQSUyMiUyMiUyQyUyMnByb2R1Y3RuYW1lJTIyJTNBJTIyJTIyJTJDJTIyc2t1JTIyJTNBJTIyJTIyJTJDJTIyYnJhbmRuYW1lJTIyJTNBJTIyJTIyJTJDJTIyc3RhdHVzJTIyJTNBJTIyMCUyMiUyQyUyMmlzdHVpamlhbiUyMiUzQSUyMiUyMiUyQyUyMnJlZmVyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnpjLnBsYXAubWlsLmNuJTJGbG9jYWxwcmljZS5odG1sJTIyJTdE\u0000"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)