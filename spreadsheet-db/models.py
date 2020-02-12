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
        return True

    def selectDB(self, sheet):
        try:
            pattern = r"(http|https)://docs.google.com/spreadsheets/.*"
            if re.search(pattern, sheet):
                self.sheet = self.client.open_by_url(sheet)
            else:
                self.sheet = self.client.open(sheet)
        except:
            raise Exception("'{}' not found or you have to authorize client email to spreadsheet".format(sheet))
        return True

    def dropDB(self, sheet):
        # NON FUNZIONA MANCO PER SBAGLIO
        '''
        .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  |     |  ,
        / `\|;-.-'|/` \
       /    |::\  |    \
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\|   |
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
       .'             `.
    _,'                 `,_
        '''
        self.client.del_spreadsheet(sheet)

    def selectTable(self, worksheet):
        self.ws = self.sheet.get_worksheet(worksheet)
        if not self.ws:
            raise Exception("Worksheet '{}' doesn't exists".format(worksheet))
        return True

    def createTable(self, title, rows=1000, cols=1000):
        self.ws = self.sheet.add_worksheet(title=title, rows=rows, cols=cols)
        return True

    def dropTable(self, worksheet):
        self.sheet.del_worksheet(self.sheet.get_worksheet(worksheet))
        return True

    def createFields(self, nameValue, primaryKey = None, overwrite = False):

        dt = {'int', 'float', 'complex', 'str', 'bool', 'list', 'tuple', 'dict'}

        if type(nameValue) != list:
            raise Exception("Expected list type, given {}".format(type(nameValue).__name__))

        for e in nameValue:
            if type(e) != tuple:
                raise Exception("Expected list of tuple, given {}".format(type(e).__name__))

        # controllo se la prima riga sia occupata da A alla lunghezza di nameValue
        actualFields = [obj.value for obj in self.ws.range('A1:{}1'.format(chr(64+len(nameValue))))]
        if actualFields.count("") != len(nameValue) and not overwrite :
            raise Exception("Table has already fields values")

        # controllo se i data-type inseriti appartengono a python
        for element in nameValue:
            if element[1] not in dt:
                raise Exception("{} is not a data type accepted".format(element[1]))

        for n,element in enumerate(nameValue):
            if element[0] == primaryKey:
                self.ws.update_acell('{}1'.format(chr(65+n)), element[0]+" [PRIMARY KEY]")
            else:
                self.ws.update_acell('{}1'.format(chr(65+n)), element[0])
                self.ws.update_acell('{}2'.format(chr(65+n)), element[1])
        return True

    def insertRow(self, value):
        if type(value) != list:
            raise Exception("Expected list, given {}".format(type(value).__name__))
        if len(value) != lenRow(self.ws, 1):
            raise Exception("Expected {} parameters, given {}".format(lenRow(self.ws, 1), len(value)))

        # check data type
        for n,obj in enumerate(value):
            expectedDT = self.ws.cell(2, n+1).value
            if str(type(obj).__name__) != expectedDT:
                raise Exception("Expected {}, given {}".format(expectedDT, type(obj).__name__))

        row = findFreeCell(self.ws)
        for n,obj in enumerate(value):
            self.ws.update_cell(row, n+1, obj)
        return True
