from flask import Flask

# 動作確認用ファイルとして作成
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

