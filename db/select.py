from .conn import connect
from model.type import Archive
from pymysql.cursors import DictCursor

connection = connect()

def select(city: str)->[]:
    result = None
    with connection.cursor(DictCursor) as cursor:
        # Create a new record
        sql = "SELECT `province`, `city`, `publish_time`, `publish_date`, `title`, `content`, `link`, `links_to_pic`, `announce_type` FROM `archives` WHERE `city`=%s"
        cursor.execute(sql, (city,))
        result = cursor.fetchall()
    return result