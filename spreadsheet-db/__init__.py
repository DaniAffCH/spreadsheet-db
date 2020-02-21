import models

__version__ = '0.0.0'
__author__ = 'Daniele Affinita'

user = "clashroyell0@gmail.com"
mydb = models.DB("../api.json")
#mydb.selectDB("tester")
#mydb.selectTable(0)
mydb.createDB("andicappatoDB", user)
#mydb.createTable("boomer")
#mydb.createFields([("bamba", "bool"), ("dim", "float")], "bamba", True)
#for c in range(3):
    #mydb.insertRow([False,float(c)])
#mydb.dropTable(2)
#mydb.dropDB("andicappatoDB")
#print(mydb.testUnique())
