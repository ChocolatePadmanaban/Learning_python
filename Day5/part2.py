# inserting Data into Mysql via python


import pymysql

db = pymysql.connect("localhost","demo","demo","test")

cursor = db.cursor()

sql = "INSERT INTO pets(name,owner,age) VALUES('%s','%s','%d')" % ('Mac','Mohan',20)

try:
    cursor.execute(sql)
except:
    db.rollback()
else:
    db.commit()

db.close()