from .conn import connect
from model.type import Archive

connection = connect()

def exist(title)->bool:
    result = False
    with connection.cursor() as cursor:
        sql = "SELECT IF(EXISTS(SELECT `id` FROM archives WHERE title = %s),  1, 0)"
        cursor.execute(sql,(title))
        if cursor.fetchone()[0] != 0:
            result = True
    return result


def insert(data: Archive):
    if exist(data.title):
        return False
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `archives` \
            (`province`,`city`,`publish_time`,`publish_date`,`title`,`content`,`link`,`links_to_pic`,`announce_type`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        cursor.execute(sql, (data.province, data.city, data.publish_time, data.publish_date, data.title, data.content, data.link,data.links_to_pic,data.announce_type))
        connection.commit()
    return True

