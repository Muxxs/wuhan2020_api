from .conn import connect
from model.type import SubLog

connection = connect()

def logInsert(log: SubLog):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `logs` \
            (`ip`, `time`, `uploader`, `province`, `city`) \
            VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(log.ip, log.time, log.uploader, log.province, log.city))

def seekByTime(limit: int):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM logs order by id desc limit %d"
        cursor.execute(sql,(limit)
        return cursor.fetchall()
