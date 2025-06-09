from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def index1():
    return render_template("index.html")


@app.route('/movie')
def movie():
    datalist = []
    sql = "select * from movieTop250"
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()
    data = c.execute(sql)
    for item in data:
        datalist.append(item)
    c.close()
    conn.close()
    return render_template("movie.html", datalist=datalist)


@app.route('/score')
def score():
    score = []
    number = []
    sql = "select score,count(score) from movieTop250 group by score"
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()
    data = c.execute(sql)
    for item in data:
        score.append(str(item[0]))
        number.append(item[1])
    c.close()
    conn.close()
    return render_template("score.html",score=score,number=number)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")



@app.route('/temp')
def temp():
    return render_template("temp.html")

if __name__ == '__main__':
    app.run()
