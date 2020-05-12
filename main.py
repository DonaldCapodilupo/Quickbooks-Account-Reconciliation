from os import path
import os


businessName = "Future Reach Marketing LLC"
bizName = ((businessName.replace(" ","+"))+"_General+Ledger.xlsx")




ROOT = path.dirname(path.realpath(__file__))
reconDirectory = os.listdir("/home/doncapodilupo/Documents/Snapshot Financials/Recons")



if __name__ == "__main__":
    print("Hello and welcome to the accounting reconciliation software V0.03")
    print("Created by Donald Capodilupo")
    from Classes.DirectoryManipulator import DirectoryManipulator
    from Classes.IndexMatch import IndexMatch
    from Classes.SpreadsheetDesigns import SpreadsheetDesigner
    confirmDownload = DirectoryManipulator("/home/doncapodilupo/Downloads")
    confirmDownload.checkDownload()
    accountAndBalanceDict = IndexMatch(bizName).getValues()
    os.chdir("/home/doncapodilupo/Documents/Snapshot Financials/Recons")
    for recon in reconDirectory:
        try:
            adjustedReconName = "Total for "+recon[:6]
            newSheet = SpreadsheetDesigner(recon, "TabName")
            newSheet.moveAndCopyWorksheet()
            try:
                newSheet.insertNewAccountBalances(accountAndBalanceDict[adjustedReconName])
            except KeyError:
                pass
        except FileNotFoundError:
            print("Error - " +recon + " will need to be created")





