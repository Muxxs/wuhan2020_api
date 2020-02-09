from .conn import connect
from model.type import SubLog
from pymysql.cursors import DictCursor

connection = connect()

def logInsert(log: SubLog):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `logs` \
            (`ip`, `time`, `uploader`, `province`, `city`) \
            VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(log.ip, log.time, log.uploader, log.province, log.city))
        connection.commit()

def seekByTime(limit: int):
    with connection.cursor(DictCursor) as cursor:
        sql = "SELECT `city`, `ip`, `province`, `time`, `uploader` FROM logs order by id desc limit %s"
        cursor.execute(sql,(limit))
        return cursor.fetchall()
