# Flaskクラスをインポート
from flask import Flask

from flask import render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

html = render_template('hello.html')

@app.route('/index')
def say_hello():
    return html

@app.route('/<city>')
def say_random(city):
    return city

if __name__ == '__main__':
    # コードが変更したタイミングでサーバーが自動でリロードされる
    app.run(debug=True)
