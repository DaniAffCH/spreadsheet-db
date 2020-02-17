import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials

# Quanti elementi sono presenti in una riga
def lenRow(worksheet, row):
    c = 0
    nextAlpha = lambda a: chr(65+a)
    while worksheet.acell('{}{}'.format(nextAlpha(c),row)).value != "":
        c += 1
    return c

#trova la prima cella libera in una colonna
def findFreeCell(worksheet, column = 1):
    counter = 4
    while worksheet.cell(counter, column).value != "":
        counter += 1
    return counter

def isUnique(worksheet, key, column = 1):
    counter = 4
    values = set()
    while worksheet.cell(counter, column).value != "":
        val = worksheet.cell(counter, column).value
        values.add(val)
        counter += 1
    if key in values:
        return False
    return True
