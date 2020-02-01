from utils import *

class DB:
    def __init__(self, api_path):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        pattern = r".+.json"
        if not re.search(pattern, api_path):
            raise Exception("{} is not a json file".format(api_path))

        creds = ServiceAccountCredentials.from_json_keyfile_name(api_path, scope)
        self.client = gspread.authorize(creds)

    def createDB(self, name, yourEmail):
        # ATTENZIONE IL FILE VIENE CREATO DALL'EMAIL DEL CLIENT API QUINDI NON SARA' VISIBILE
        # PER RISOLVERE BISOGNA CONDIVIDERE IL FILE CON SE STESSI
        self.sheet = self.client.create(name)
        self.sheet.share(yourEmail, perm_type='user', role='writer')

    def selectDB(self, sheet):
        try:
            pattern = r"(http|https)://docs.google.com/spreadsheets/.*"
            if re.search(pattern, sheet):
                self.sheet = self.client.open_by_url(sheet)
            else:
                self.sheet = self.client.open(sheet)
        except:
            raise Exception("'{}' not found or you have to authorize client email to spreadsheet".format(sheet))

    def selectTable(self, worksheet):
        self.ws = self.sheet.get_worksheet(worksheet)
        if not self.ws:
            raise Exception("Worksheet '{}' doesn't exists".format(worksheet))

    def createTable(self, title, rows=1000, cols=1000):
        self.ws = self.sheet.add_worksheet(title=title, rows=rows, cols=cols)

    def createFields(self, nameValue, overwrite = False):
        if type(nameValue) != list:
            raise Exception("Expected list type, given {}".format(type(nameValue).__name__))

        for e in nameValue:
            if type(e) != tuple:
                raise Exception("Expected list of tuple, given {}".format(type(e).__name__))

        # controllo se la prima riga sia occupata da A alla lunghezza di nameValue
        actualFields = [obj.value for obj in self.ws.range('A1:{}1'.format(chr(64+len(nameValue))))]
        if actualFields.count("") != len(nameValue) and not overwrite :
            raise Exception("Table has already fields values")
        for n,element in enumerate(nameValue):
            self.ws.update_acell('{}1'.format(chr(65+n)), element[0])
            self.ws.update_acell('{}2'.format(chr(65+n)), element[1])
