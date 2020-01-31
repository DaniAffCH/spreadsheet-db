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

    def openSheet(self, sheet):
        try:
            pattern = r"(http|https)://docs.google.com/spreadsheets/.*"
            if re.search(pattern, sheet):
                self.sheet = self.client.open_by_url(sheet)
            else:
                self.sheet = self.client.open(sheet)
        except:
            raise Exception("'{}' not found or you have to authorize client email to spreadsheet".format(sheet))

    def selectWorksheet(self, worksheet):
        self.ws = self.sheet.get_worksheet(worksheet)
        if not self.ws:
            raise Exception("Worksheet '{}' doesn't exists".format(worksheet))

    def createWorksheet(self, title, rows=999, cols=999):
        self.ws = self.sheet.add_worksheet(title=title, rows=rows, cols=cols)
