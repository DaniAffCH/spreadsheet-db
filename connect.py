import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
class Connect:

    def __init__(self, api_path):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        pattern = r".+.json"
        if not re.search(pattern, api_path):
            raise Exception("{} is not a json file".format(api_path))

        creds = ServiceAccountCredentials.from_json_keyfile_name(api_path, scope)
        self.client = gspread.authorize(creds)

    def openSheet(self, sheet, worksheet=0):
        try:
            pattern = r"(http|https)://docs.google.com/spreadsheets/.*"
            if re.search(pattern, sheet):
                self.sheet = client.open_by_url(sheet)
            else:
                self.sheet = client.open(sheet).sheet1
        except:
            raise Exception("{} not found".format(sheet))
        #ws = self.sheet.get_worksheet(worksheet)

    def createTable(self, name, worksheet_name, fields, worksheet_size = (1000,1000)):
        #crea foglio
        sh = self.client.create(name)
        #crea worksheet
        worksheet = sh.add_worksheet(title = worksheet_name, rows=worksheet_size[0], cols=worksheet_size[1])
        cell_list = worksheet.range('A1:A{}'.format(len(fields)))
        for c in range(len(fields)):
            cell_list[c].value = fields[c]
        return True
