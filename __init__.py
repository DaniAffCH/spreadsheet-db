import pyxhook
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import unicodedata

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("api.json", scope)
client = gspread.authorize(creds)

sheet = client.open("tester").sheet1

label = dict()
y = 1

while sheet.cell(1,y).value != "":
    label[sheet.cell(1,y).value] = y
    y += 1


def addValue(field, value):
    if field not in label:
        raise Exception("field doesn't exists")
    x = 1
    while sheet.cell(x,label[field]).value != "":
        x+=1
    sheet.update_cell(x,label[field],value)
    return True

def addRow(values):
    if(type(values).__name__ != "list"):
        raise Exception("expected a list, given {}".format(type(values).__name__))
    if len(label) != len(values):
        raise Exception("expected {} argument, given {}".format(len(label), len(values)))


addRow([1,2,3,4])
