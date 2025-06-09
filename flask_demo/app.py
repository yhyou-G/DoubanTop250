from flask import Flask
from flask import render_template  # 为返回html文件准备
from flask import request

import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


'''
    flask框架预备知识：
    1. flask包含Werkzeug（帮助找到路径）、Jinja2（返回啥！！（如html））
    2. 开启debug模式，实时查看更新效果，以及错误提示(一定开):
        如何开：找到菜单栏Flask(app.py),点击EditConfigurations-->勾上FLASK DEBUG
    3.返回渲染后的html网页文件：
        准备工作:引入from flask import render_template
'''


# 1.通过访问路径，获取字符串参数（可以多个，用<>表示）
@app.route('/student/<major>/<name>')
def student_info(major, name):
    return '你好,%s%s' % (major, name)


# 2.通过访问路径，获取整形参数
@app.route('/user/<int:id>')
def usr_info(id):
    return '你好,%d号会员' % id


# 3.返回渲染后的html网页文件（在templates中建html文件）
###准备工作:引入from flask import render_template
# @app.route('/index')
# def index():
#     return render_template('index.html')


# 向页面传递一个变量
@app.route('/index/')
def index():
    today = datetime.date.today()  # 普通变量
    name = ['kk', '飘啊飘', '二火']  # 列表
    dic = {'age': '20', "sex": "女"}  # 字典
    return render_template('index.html', var=today, list=name, dic=dic)


# 提交表单
@app.route('/test/register')
def register():
    return render_template('test/register.html')


# 在resgister.html中提交表单的方式是post,此处路由方法也需要设置为'POST',默认不设置的话为'GET'
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('test/result.html', result=result)


if __name__ == '__main__':
    app.run()
