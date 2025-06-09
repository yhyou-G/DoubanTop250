# coding=utf-8
# @author: yyh
# @time  : 2020/10/30 19:39

import jieba  # 分词
from PIL import Image  # 图像处理
import numpy as np  # 矩阵运算
from wordcloud import WordCloud  # 词云
from matplotlib import pyplot as plt  # 绘图，数据可视化
import sqlite3

conn = sqlite3.connect("movie.db")
c = conn.cursor()
sql = "select instruction from movieTop250"
data = c.execute(sql)
text = ''
for item in data:
    text = text + item[0]
print(text)
c.close()
conn.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(string)
print(len(string))

#准备输出图片的格式（背景颜色，字体等），需要用到遮罩图片
img = Image.open('static/assets/img/tree.jpg')  #打开遮罩图片
img_array = np.array(img)   #将图片转化为数组
wc = WordCloud(
    background_color='white',#输出图片
    mask=img_array,
    font_path="STXINGKA.TTF"
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)  #按照wc的规则显示图片
plt.axis('off')  # 是否显示坐标

plt.show()  #显示生成的词云图片

# 输出词云图片到文件
#plt.savefig('static/assets/img/word.jpg', dip=600)
