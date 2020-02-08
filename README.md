# wuhan2020_api
wuhan2020数据库 API接口

version 0.0.1



### 提交数据

> POST http://wuhan2020.muxxs.com/api/add

| 字段          | 说明     |
| ------------- | -------- |
| announce_type | 默认 “0” |
| city          | 市级名   |
| content       | 主要内容 |
| link          | 原文链接 |
| links_to_pic  | 图片链接 |
| province      | 省名     |
| publish_date  | 发布日期 |
| publish_time  | 发布时间 |
| title         | 标题     |

#### 使用python3提交数据

> title重复会被判断为已存在

```python
import json
from urllib import request

headers = {'Content-Type': 'application/json'}

data = {
    'province': "test",
    'city': 'test',
    'publish_time': '00:00:00',
    'publish_date': '0',
    'title': 'teeeeeeeeeee',
    'content': "测试测试测试",
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
```



### 获取数据

#### 通过城市获取数据

>GET http://wuhan2020.muxxs.com/api/read?city=<城市名>

例如

GET http://wuhan2020.muxxs.com/api/read?city=test

```json
{
  "code": 0,
  "message": "成功",
  "data": [
    {
      "announce_type": "0",
      "city": "test",
      "content": "ttttttttttttttttttttt",
      "link": "http://test.test",
      "links_to_pic": "teeeeeeessst",
      "province": "test",
      "publish_date": "0000-00-00",
      "publish_time": "00:00:00",
      "title": "test"
    }
  ]
}
```

