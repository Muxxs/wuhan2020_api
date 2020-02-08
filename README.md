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

例如

```json
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

