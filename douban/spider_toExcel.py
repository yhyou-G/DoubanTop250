# coding=utf-8
# @author: yyh
# time on: 2020/10/27 13:19

# import bs4
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，文字匹配
import urllib.request, urllib.error  # 指定url,获取网页数据
import xlwt  # 进行excel操作



def main():
    beseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    datalist = getData(beseurl)
    savepath = '豆瓣电影Top250.xls'
    # 3.保存数据
    saveData(datalist, savepath)


# 影片链接的正则表达式对象，如<a href="https://movie.douban.com/subject/1292052/">
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片的正则表达式对象，
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中(忽视换行符带来的干扰)
# 影片名字
findTitles = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 1.爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 10页
        url = baseurl + str(i * 25)  # 每页25条(url=基本路径+i*25,0<=i<=10)
        html = askUrl(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)    #查看电影所有信息
            data = []  # 保存一部电影的全部信息
            item = str(item)

            link = re.findall(findLink, item)[0]  # 影片详情链接
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]  # 图片
            data.append(imgSrc)

            titles = re.findall(findTitles, item)  # 除了中文名，可能还含有外文名
            if len(titles) == 2:  # 有两个名字
                ctitle = titles[0]
                data.append(ctitle)  # 添加中文名
                otitle = titles[1].replace("/", "")
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])  # 只有中文名
                data.append(' ')  ###外国名留空

            score = re.findall(findScore, item)[0]  # 评分
            data.append(score)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inq = re.findall(findInq, item)  # 概况，可能有，也可能没有
            if len(inq) != 0:
                data.append(inq[0].replace("。", ""))
            else:
                data.append(' ')

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)  # 去掉<br/>
            bd = re.sub('/', ' ', bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  ####### 将处理好的一部电影信息放进datalist
    print(datalist)
    return datalist


# 得到一个指定的url网页内容
def askUrl(url):
    '''
       head:
       1.模拟（伪装）浏览器头部信息，向豆瓣服务器发送消息
       2.用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器
       （本质上是告诉浏览器，我们可以接受什么水平的文件内容）
    '''
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 "
                      "Safari/537.36 "
    }
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接', '图片链接', '影片中文名', '影片英文名', '评分', '评价书', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print('第%d条' % i, datalist[i])
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存数据表
    print('爬取完毕！！')


if __name__ == '__main__':
    main()
