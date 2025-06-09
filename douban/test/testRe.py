# coding=utf-8
# @author: yyh
# time on: 2020/10/28 9:03

# 正则表达式
import re

# ----------1.用research()
# 创建模式对象
pat = re.compile('\d{3}')  # 正则表达式
m = pat.search('123')  # 被校验字符串
print(m)

# 没有模式对象
m = re.search('[A-Z]', 'ADadsBCKj')  # 前面是正则表达式,后面是被检验字符串
print(m)


# ----------2.用findall()
print(re.findall('[A-Z]', 'ADadsBCKj')) # 前面是正则表达式,后面是被检验字符串
print(re.findall('[A-Z]+', 'ADadsBCKj'))

# ----------3.用sub()
print(re.sub('a', 'A', 'aaabbbaC'))  # 用A替换字符串aaabbbaC中的所有a

###建议在正则表达式中，被比较的字符串前面加上r,防止字符转义
a = "\aab-\""
b = r"\aab-\""
print(a)
print(b)
