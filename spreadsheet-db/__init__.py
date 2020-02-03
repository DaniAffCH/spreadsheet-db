import models

__version__ = '0.0.0'
__author__ = 'Daniele Affinita'

mydb = models.DB("../api.json")
mydb.selectDB("tester")
mydb.selectTable(0)
#mydb.createSheet("prova123", "danieleaffinita2000@gmail.com")
#mydb.createWorksheet("boomer")
#mydb.createFields([("bamba", "bool"), ("dim", "float")], True)
mydb.insertRow([False,1.00,4])
