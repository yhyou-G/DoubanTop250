# coding=utf-8
# @author: yyh
# time on: 2020/10/28 15:36

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
worksheet.write(0, 0, 'hello')  # 写入数据，三个参数分别表示：行，列，内容
workbook.save('student.xls')  # 保存数据表

#在excel表中输出九九乘法表
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('九九乘法表')
for i in range(1, 10):
    for j in range(1, i + 1):
        worksheet.write(i-1,j-1,'%d*%d=%d' % (j, i, j * i))
workbook.save('chengfabiao.xls')
