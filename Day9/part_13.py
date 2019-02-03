# writting a json file


import json
mycompounds = [{"name":"Fructose","formula": "C6H1206","id":79025,
"similarTo":["Hexose", "Glucose"]}]
with open("someFile.json", "w") as jsonFile:
    json.dump( mycompounds, jsonFile)


# reading a json file

with open("someFile.json","r") as jsonFile:
    compounds = json.load(jsonFile)
print(compounds[0]["name"]) #=> Glucose
print(compounds[0]["formula"]) #=> true

