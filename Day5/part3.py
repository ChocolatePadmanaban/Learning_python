# Fetching rows form MySQL using Python

import pymysql

db = pymysql.connect("localhost","demo","demo", "test")

cursor = db.cursor()

age = int(input("Enter the age:  "))

sql = "SELECT * FROM pets WHERE age < %d" % (age)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name = row[0]
        owner = row[1]
        age = row[2]
        print("name= %s , owner= %s, age= %d"% (name, owner, age))
except:
    print("Error: Unable to fetch data")        
        
db.close()