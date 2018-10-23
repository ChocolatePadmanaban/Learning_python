# Updating MySQL database using python

import pymysql

db = pymysql.connect("localhost","demo","demo", "test")

cursor = db.cursor()

sql = "UPDATE pets SET age = age + 1 WHERE age>12"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()        
        
db.close()