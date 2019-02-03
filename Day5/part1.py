# Connecting to MySql database

import pymysql

db = pymysql.connect("localhost",'demo','demo','test')

cursor = db.cursor()


cursor.execute("SELECT VERSION()")


data =cursor.fetchone()

print('Database version : %s ' % data)

db.close()