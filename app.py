#coding=utf-8
from flask import Flask,request
import pymysql


app: Flask = Flask(__name__)



@app.route('/',methods=['POST'])
def hello_world():
    if request.method=="POST":
        get_infor = request.get_json()
        print(get_infor['province'])
        data = {
            'province': "",
            'city': '0',
            'publish_time': '00:00:00',
            'publish_date': 0,
            'title': 0,
            'content': 0,
            'link': 0,
            'links_to_pic': 0,
            'announce_type': 0
        }
        key = get_infor['key']
        if key!="123":
            print("wrong key")
            return "KEY WRONG"
        province=get_infor['province']
        city=get_infor['city']
        publish_time=get_infor['publish_time']
        publish_date=get_infor['publish_date']
        title=get_infor['title']
        content=get_infor['content']
        link=get_infor['link']
        links_to_pic=get_infor['links_to_pic']
        announce_type=get_infor['announce_type']

        db = pymysql.connect('localhost', 'wuhan2020', 'For_wuhan2020', 'data_test', charset='utf8',port=3306)
        
        #数据库操作
        
        cursor = db.cursor()



        db.close()
        return 'Hello World!'
    return "HI"

def get_data():
    print("get date")

if __name__ == '__main__':
    app.run()

