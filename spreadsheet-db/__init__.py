import models

__version__ = '0.0.0'
__author__ = 'Daniele Affinita'

mydb = models.DB("../api.json")
mydb.openSheet("tester")
mydb.createWorksheet("boomer")
