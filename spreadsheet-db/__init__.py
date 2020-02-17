import models

__version__ = '0.0.0'
__author__ = 'Daniele Affinita'

mydb = models.DB("../api.json")
mydb.selectDB("tester")
mydb.selectTable(0)
#mydb.createDB("cancellami", "danieleaffinita2000@gmail.com")
#mydb.createWorksheet("boomer")
#mydb.createFields([("bamba", "bool"), ("dim", "float")], "bamba", True)
#for c in range(3):
    #mydb.insertRow([False,float(c)])
#mydb.dropTable(2)
#mydb.dropDB("cancellami")
print(mydb.testUnique())
