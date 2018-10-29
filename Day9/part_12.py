#using for loop to iterate over a tree which is the xml fiel

from xml.dom import minidom

doc = minidom.parse("breakfast.xml")

name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

foods = doc.getElementsByTagName("food")

for food in foods:
    mid = food.getAttribute("menuid")
    desc = food.getElementsByTagName("description")[0]
    cal = food.getElementsByTagName("calories")[0]

    print("menuid: %s, description: %s, calories: %s" % (mid,desc.firstChild.data,cal.firstChild.data))