import pymysql.cursors

# Connect to the database
import os

def GetEnvPassword():
    if os.getenv("PASSWORD") == None:
        return "password"
    return os.getenv("PASSWORD")

def connect()->pymysql.Connection:
   return pymysql.connect(
        host='localhost',
        user='root',
        password = GetEnvPassword(),
        db='db',
        charset='utf8mb4'
    )
