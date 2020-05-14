
class SpreadsheetDesigner:
    def __init__(self, workbook, tabName, directory):
        self.workbook = workbook
        self.tabName = tabName
        self.directory = directory


    def moveAndCopyWorksheet(self):

        from openpyxl import load_workbook
        from openpyxl.utils.exceptions import InvalidFileException
        try:
            wb = load_workbook(self.directory+"/"+self.workbook)
            currentSheet = wb.active
            previousSheet = currentSheet
            newSheet = wb.copy_worksheet(previousSheet)
            newSheet.title = self.tabName
            wb.save(self.workbook)
        except InvalidFileException:
            print("Not an excel file extension - "+ self.workbook)


    def insertNewAccountBalances(self, accountBalance):
        from openpyxl import load_workbook
        wb = load_workbook(self.directory+"/"+self.workbook)
        ws = wb[self.tabName]
        ws["J4"] = accountBalance
        wb.save(self.workbook)

