from os import path
import os

from SetupTool import getMonthlyFolderTitle
businessName = "Future Reach Marketing LLC"
ROOT = path.dirname(path.realpath(__file__))
reconDirectory = ROOT+"/Recons"
monthlyFolderDirectory = (reconDirectory+"/"+getMonthlyFolderTitle())


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
    #os.chdir("/home/doncapodilupo/Documents/Snapshot Financials/Recons")
    keyErrors = []

    for recon in os.listdir(reconDirectory):
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
            #from Classes.ListDisplay import ListDisplay
            #from SetupTool import getMonthlyFolderTitle
            #os.chdir(ROOT+"/Recons/"+str(getMonthlyFolderTitle()))
            #reconOptions = ["Single Recon", "Double Recon"]
            #print("What account type is " + str(recon)+"?")
            #single_Or_Double_Recon = ListDisplay(reconOptions)
            #single_Or_Double_Recon.displayList(False)
            #ewRecon = SpreadsheetCreator(recon,"Other",getTabName())
            #ry:
            #    adjustedReconName = "Total for " + recon[:6]
            #    newSheet = SpreadsheetDesigner(recon, getTabName())
            #    newSheet.moveAndCopyWorksheet()
            #    try:
            #        newSheet.insertNewAccountBalances(accountAndBalanceDict[adjustedReconName])
            #        print("This account has had activity and the recon has been updated: " + recon)
            #        del accountAndBalanceDict[adjustedReconName]
            #    except KeyError:
            #        print("This account has not had any activity during this time frame: " + recon)
            #        pass
            #except KeyError:
            #    print("Somehow a key error: "+recon)
    from Classes.SpreadsheetCreator import SpreadsheetCreator
    from Classes.ListDisplay import ListDisplay

    for workbook in accountAndBalanceDict.keys():
        #os.chdir(ROOT+"/Recons/"+getMonthlyFolderTitle())
        print("There is not a workbook for "+workbook+" created in the directory.")
        print("Creating workbook af file location: "+str(ROOT)+"/Recons/"+getMonthlyFolderTitle())
        reconOptions = ["Single Recon", "Double Recon"]
        print("What account type is " + str(workbook) + "?")
        single_Or_Double_Recon = ListDisplay(reconOptions)
        reconChoice = single_Or_Double_Recon.displayList(False)

        if reconChoice == 'Single Recon':
           newSingleReconWorkbook = SpreadsheetCreator(workbook, getTabName(), monthlyFolderDirectory)
           #os.chdir(ROOT+"/Recons/"+getMonthlyFolderTitle())
           newSingleReconWorkbook.singleAccountReconcilliationformat()
        else:
            newSingleReconWorkbook = SpreadsheetCreator(workbook, getTabName(), monthlyFolderDirectory)
            #os.chdir(ROOT + "/Recons/" + getMonthlyFolderTitle())
            newSingleReconWorkbook.doubleAccountReconcilliationformat()








    #    if accountNumber in






