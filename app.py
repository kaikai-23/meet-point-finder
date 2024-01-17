# Flaskクラスをインポート
from flask import Flask
# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/index')
def say_hello():
    return "Hello Index"

if __name__ == '__main__':
    app.run(debug=True)
