
class SpreadsheetUpdater:
    def __init__(self, directory, dictAccounts_and_Values, businessName):
        self.directory = directory
        self.dictAccountAndValues = dictAccounts_and_Values
        self.businessName = businessName

    def convertDictToList(self):
        accountNums = []

        for key in self.dictAccountAndValues.keys():
            accountNums.append(key[-6:])
        return accountNums

    def easyUpdate(self, reconName):
        from openpyxl import load_workbook
        wb = load_workbook(filename=reconName)
        sheet = wb.active
        sheet["A9"] = "Tits"
        wb.save(reconName)


    def getAccountsThatCanBeUpdatedEasily(self):
        import os
        os.chdir(self.directory)
        reconDirectory = os.listdir(self.directory) #100500 Checking .xlsx
        dictionaryList = self.convertDictToList() #[[100500],
        accountsToUpdateSeparately = {"Accounts that haven't had activity":[],
                                      "Accounts that have no recons":[]}


        for recon in reconDirectory:
            reconNumber = recon[0:6]
            if reconNumber in dictionaryList:
                self.easyUpdate(recon)
                dictionaryList.remove(reconNumber)
            if reconNumber not in dictionaryList:
                accountsToUpdateSeparately["Accounts that have no recons"].append(recon)
        for i in dictionaryList:
            accountsToUpdateSeparately["Accounts that haven't had activity"].append(i)


        print(accountsToUpdateSeparately)









businessName = "Future Reach Marketing LLC"
bizName = ((businessName.replace(" ","+"))+"_General+Ledger.xlsx")
from Classes.IndexMatch import IndexMatch
cat = SpreadsheetUpdater("/home/doncapodilupo/Documents/Snapshot Financials/Recons",IndexMatch(bizName).getValues(),
                         bizName)
cat.getAccountsThatCanBeUpdatedEasily()