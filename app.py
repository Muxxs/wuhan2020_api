#coding=utf-8
from flask import Flask, request
from control import readCtl, writeCtl

app: Flask = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(readCtl)
app.register_blueprint(writeCtl)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80")

