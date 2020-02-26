import models

__version__ = '0.0.0'
__author__ = 'Daniele Affinita'

user = "clashroyell0@gmail.com"
mydb = models.DB("../api.json")

#------------------------------------------------------------------------------------------------------
#Creazione di un Database e di alcune Tabelle
#mydb.createDB("andicappatoDB", user)
#mydb.createTable("boomer")
#mydb.createFields([("bamba", "bool"), ("dim", "float")], "bamba", True)
#for c in range(3):
#mydb.insertRow([False,float(c)])

#------------------------------------------------------------------------------------------------------
#Selezione di un Database
mydb.selectDB("tester")
mydb.selectTable("Foglio1")

#------------------------------------------------------------------------------------------------------
#Eliminazione di un Database/di Tabelle
#mydb.dropTable(2)
#mydb.dropDB("andicappatoDB")
#print(mydb.testUnique())

#------------------------------------------------------------------------------------------------------
#Test vari
mydb.insertRow(["", ""])