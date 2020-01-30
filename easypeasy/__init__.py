import os
import pyxhook
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import unicodedata

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("../api.json", scope)
client = gspread.authorize(creds)

# <class 'gspread.models.Worksheet'>
sheet = client.open("tester").sheet1
