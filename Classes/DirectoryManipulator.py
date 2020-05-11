businessName = "Future Reach Marketing LLC"

class DirectoryManipulator:
    def __init__(self,directory):
        self.directory = directory
        self.fileName = ((businessName.replace(" ","+"))+"_General+Ledger.xlsx")

    def checkDownload(self):
        import os
        print("Checking the downloads folder.")
        if self.fileName in os.listdir(self.directory):
            print("File is present in the downloads folder")
            return True
        else:
            print("There is no file titled "+self.fileName+" in "+self.directory+".")
            print("Please download it and run the program again.")
            exit()
    def getDirectoryList(self):
        import os
        return os.listdir(self.directory)

    def convertToCSV(self, mainDirectory):
        import pandas as pd
        import os
        # Code will go here to change the directory to the downloads folder.
        os.chdir(mainDirectory)
        data_xls = pd.read_excel(self.fileName, 'General Ledger',
                                 index_col=None)  # THIS CODE CONVERTS THE EXCEL DOWNLOAD TO A CSV
        os.chdir(mainDirectory)
        data_xls.to_csv('General Ledger.csv', encoding='utf-8')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)  # not sure what these do.

    def findAccountsToRecon(self):
        import pandas as pd
        df = pd.read_csv('General Ledger.csv')  # creates an opject for the open CSV
        totalsrowindex = (df[df['Total for'].str.contains(
            "Total for") == True])  # gives me a list of all of the rows that have "total" in them
        rowswithtotal = totalsrowindex.astype(
            int).values.tolist()  # Converts pandas/csv into INT type instead of some "type64 INT" bullshit
        accountstobereconcilled = []  # allows me to remove unwanted data. May be redundant not sure
        for keys in rowswithtotal:
            if keys != 'nan':
                accountstobereconcilled.append(keys[1])
        accountsThatNeedToBeReconned = []
        for recon in accountstobereconcilled:
            accountsThatNeedToBeReconned.append(
                recon[10:19])
        return accountsThatNeedToBeReconned  # List of accounts that need to be reconciled.










