
class SpreadsheetDesigner:
    def __init__(self, workbook, tabName):
        self.workbook = workbook
        self.tabName = tabName


    def moveAndCopyWorksheet(self):

        from openpyxl import load_workbook
        wb = load_workbook(self.workbook)
        previousSheet = wb.active
        newSheet = wb.copy_worksheet(previousSheet)
        newSheet.title = self.tabName

        wb.save(self.workbook)

    def insertNewAccountBalances(self, accountBalance):
        from openpyxl import load_workbook
        wb = load_workbook(self.workbook)
        ws = wb.active
        ws["J4"] = accountBalance
        wb.save(self.workbook)



import os
os.chdir("/home/doncapodilupo/Documents/Snapshot Financials/Recons")


recons = ["100500 - Business Fundamentals Chk.xlsx",
          "110000 - Accounts Receivable.xlsx"]
for recon in recons:
    cat = SpreadsheetDesigner(recon,"051120")
    cat.moveAndCopyWorksheet()
    cat.insertNewAccountBalances("25.64")