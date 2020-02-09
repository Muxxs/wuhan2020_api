import json
from urllib import request

headers = {'Content-Type': 'application/json'}

data = {
    'province': "test",
    'city': 'test',
    'publish_time': '00:00:00',
    'publish_date': '0',
    'title': 'python3urllib',
    'content': "python3 urllib post 提交",
    'link': "http://wsjkw.hebei.gov.cn/content/content_45/395747.whtml",
    'links_to_pic': '0',
    'announce_type': 0
}

req = request.Request(
    url="http://152.136.160.189/api/add", 
    headers=headers,
    data=json.dumps(data, ensure_ascii=False).encode("UTF-8")
)

res = request.urlopen(req)
print(res.read().decode("utf-8"))