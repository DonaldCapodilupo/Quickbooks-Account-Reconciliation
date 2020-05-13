from os import path
import os


businessName = "Future Reach Marketing LLC"
ROOT = path.dirname(path.realpath(__file__))
reconDirectory = os.listdir(ROOT+"/Recons")


def getTabName():
    import datetime
    current_time = datetime.datetime.now()
    monthlyFolderTitle = current_time.strftime('%m%d%y')
    return monthlyFolderTitle

if __name__ == "__main__":
    print("Hello and welcome to the accounting reconciliation software V0.03")
    print("Created by Donald Capodilupo")
    from Classes.DirectoryManipulator import DirectoryManipulator
    from Classes.IndexMatch import IndexMatch
    from Classes.SpreadsheetDesigns import SpreadsheetDesigner
    from Classes.SpreadsheetCreator import SpreadsheetCreator
    from SetupTool import *
    directorySetup()
    confirmDownload = DirectoryManipulator("/home/doncapodilupo/Downloads", businessName).checkDownload()
    accountAndBalanceDict = IndexMatch(((businessName.replace(" ","+"))+"_General+Ledger.xlsx")).getValues()
    os.chdir("/home/doncapodilupo/Documents/Snapshot Financials/Recons")
    keyErrors = []

    for recon in reconDirectory:
        os.chdir(ROOT+"/Recons")
        try:
            adjustedReconName = "Total for "+recon[:6]
            newSheet = SpreadsheetDesigner(recon, getTabName())
            newSheet.moveAndCopyWorksheet()
            try:
                newSheet.insertNewAccountBalances(accountAndBalanceDict[adjustedReconName])
                print("This account has had activity and the recon has been updated: " +recon)
                del accountAndBalanceDict[adjustedReconName]
            except KeyError:
                print("This account has not had any activity during this time frame: "+recon)
                pass
        except FileNotFoundError:
            print("Error - " +recon + " will need to be created")
            from Classes.ListDisplay import ListDisplay
            from SetupTool import getMonthlyFolderTitle
            os.chdir(ROOT+"/Recons/"+str(getMonthlyFolderTitle()))
            reconOptions = ["Single Recon", "Double Recon"]
            #print("What account type is " + str(recon)+"?")
            #single_Or_Double_Recon = ListDisplay(reconOptions)
            #single_Or_Double_Recon.displayList(False)
            newRecon = SpreadsheetCreator(recon,"Other",getTabName())
            try:
                adjustedReconName = "Total for " + recon[:6]
                newSheet = SpreadsheetDesigner(recon, getTabName())
                newSheet.moveAndCopyWorksheet()
                try:
                    newSheet.insertNewAccountBalances(accountAndBalanceDict[adjustedReconName])
                    print("This account has had activity and the recon has been updated: " + recon)
                    del accountAndBalanceDict[adjustedReconName]
                except KeyError:
                    print("This account has not had any activity during this time frame: " + recon)
                    pass
            except KeyError:
                print("Somehow a key error: "+recon)




    print(accountAndBalanceDict)

    #    if accountNumber in






