# coding=utf-8
# @author: yyh
# time on: 2020/10/27 20:54

from bs4 import BeautifulSoup

file = open('./baidu.html', 'rb')
html = file.read().decode('utf-8')      #读取文档
bs = BeautifulSoup(html, 'html.parser') #指定解析器解析文档，获得文档对象
# print(bs.title)
# print(bs.head)
# print(bs.a)

# #1. Tag 标签及其内容：拿到它所找到的第一个内容
# print(bs.title.string)
# print(type(bs.title.string))

# #2.NavigableString 标签里的内容（字符串）
# print(bs.a.attrs)

# #3.BeautifulSoup表示整个文档
# print(bs)

# #4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号



########文档的搜索

#-------1.find_all--------
#字符串过滤：会查找与字符串完全匹配的内容
# a_list = bs.find_all("a")
# print(a_list)


#-------2.引入正则表达式模块（很常用）
# 正则表达式搜索：使用search()方法来匹配内容
import re
a_list = bs.find_all("span",class_='sence-block-hover')
for item in a_list:
    print(item)


#--------2.kwargs 参数
#例：打印id为head 的元素内容
# head_list = bs.find_all(id="head")
# for item in head_list:
#     print(item)
# head_list = bs.find_all(class_="news-meta-item clearfix")
# #例：打印class=news-meta-item clearfix 的元素内容，class_，下划线不能掉
# for item in head_list:
#     print(item)


#--------3.text 参数
# text_list = bs.find_all(text='hpyouyu')                 #一个内容
# print(text_list)
# text_list = bs.find_all(text=['hpyouyu','地图','新闻'])  #多个内容
# print(text_list)

#--------4.limit 参数
# a_list = bs.find_all("a",limit=50)
# for item in a_list:
#     print(item)

#--------css选择器
#t_list = bs.select('title') #通过标签来查找
#t_list = bs.select('.mnav') #通过类名来查找
#t_list = bs.select('#u1')   #通过id来查找
#t_list = bs.select('a[class="mnav c-font-normal c-color-t"]')  # 通过id来查找
#t_list = bs.select('head > meta')   #通过子标签来查找
# for item in t_list:
#     print(item)


# t_list = bs.select(".mnav ~ .bri") #获取与"mnav 标签的第一个兄弟节点",报错是因为没有
# print(t_list[0].get_text())



#方法：传入一个函数（方法），根据函数的要求来搜索，反回含有"name"属性的标签(可用于自定义)，了解一下就行
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# name_list = bs.find_all(name_is_exists)
# print(name_list)




