# coding=utf-8
# @author: yyh
# time on: 2020/10/27 15:01

import urllib.request
# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")  # 爬豆瓣网 http://douban.com，打印状态信息：HTTP Error 418：被发现正在爬
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码，打印
# print('状态码：', response.status)  # 200
# print('获得所有头部信息:', response.getheaders())
# print('获得头部信息中的一个:', response.getheader('Cache-Control'))
# try:
#     # 0.01s内没响应：超时处理，捕获异常，使程序更健壮
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01) #timeout=更大即可
#     #print(response.read().decode('utf-8'))
#     #print('------------------------------------------------')
# except urllib.error.URLError as result:
#     print("time out!!")


# 获取一个post请求
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode('utf-8'))
# '''
#     输出"header"中的"User-Agent": "Python-urllib/3.5",
# '''

# 例子，为以下模拟浏览器访问豆瓣网做铺垫
# url = "http://httpbin.org/post"
'''
  headers:
  1.模拟浏览器头部信息，向豆瓣服务器发送消息
  2.用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器
  （本质上是告诉浏览器，我们可以接受什么水平的文件内容）
'''
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name': 'youyinghui', 'ps': '123'}), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# 模拟浏览器访问豆瓣网
url="http://douban.com"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)#需要headers(一定要)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
