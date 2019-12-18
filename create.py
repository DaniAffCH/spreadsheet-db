import connect
class Create(connect.Connect):
    def __init__(self):
        pass
    def table(self, name, fields):
        sh = self.client.create(name)
        cell_list = worksheet.range('A1:A{}'.format(len(fields)))
        for c in range(len(fields)):
            cell_list[c].value = fields[c]
        return True
