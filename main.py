from os import path
import os

from SetupTool import getMonthlyFolderTitle
businessName = "Future Reach Marketing LLC"
ROOT = path.dirname(path.realpath(__file__))
reconDirectory = ROOT+"/Recons"
monthlyFolderDirectory = (ROOT+"/Recons/"+getMonthlyFolderTitle())


def getTabName():
    import datetime
    current_time = datetime.datetime.now()
    monthlyFolderTitle = current_time.strftime('%m%d%y')
    return monthlyFolderTitle

if __name__ == "__main__":
    print("Hello and welcome to the accounting reconciliation software V1.00")
    print("Created by Donald Capodilupo")
    from Classes.DirectoryManipulator import DirectoryManipulator
    from Classes.IndexMatch import IndexMatch
    from Classes.SpreadsheetDesigns import SpreadsheetDesigner
    from Classes.SpreadsheetCreator import SpreadsheetCreator
    from SetupTool import *
    directorySetup()
    confirmDownload = DirectoryManipulator("C:\\Users\Don\Downloads", businessName).checkDownload()
    accountAndBalanceDict = IndexMatch(((businessName.replace(" ","+"))+"_General+Ledger.xlsx")).getValues()
    os.chdir(monthlyFolderDirectory)

    from Classes.ListDisplay import ListDisplay

    tabDecisions = [getTabName(),"Custom Tab Name"]

    tabName = ListDisplay(tabDecisions)
    tabName.displayList(False)
    if tabName == getTabName():
        pass
    else:
        print("What would you like the tab name to be?")
        tabName = input(">")

    for recon in os.listdir(monthlyFolderDirectory):
        try:
            newSheet = SpreadsheetDesigner(recon, tabName,monthlyFolderDirectory)
            newSheet.moveAndCopyWorksheet()
            try:
                newSheet.insertNewAccountBalances(accountAndBalanceDict[recon])
                print("This account has had activity and the recon has been updated: " +recon)
                del accountAndBalanceDict[recon]
            except KeyError:
                print("This account has not had any activity during this time frame: "+recon)
                pass
        except FileNotFoundError:
            print("Error - " +recon + " will need to be created")

    from Classes.SpreadsheetCreator import SpreadsheetCreator


    for workbook in accountAndBalanceDict.keys():
        workbook = str(workbook).replace("/","")
        print("There is not a workbook for "+workbook+" created in the directory.")
        print("Creating workbook af file location: "+str(ROOT)+"/Recons/"+getMonthlyFolderTitle())
        reconOptions = ["Single Recon", "Double Recon"]
        print("What account type is " + str(workbook) + "?")
        single_Or_Double_Recon = ListDisplay(reconOptions)
        reconChoice = single_Or_Double_Recon.displayList(False)

        if reconChoice == 'Single Recon':
           newSingleReconWorkbook = SpreadsheetCreator(workbook, tabName, monthlyFolderDirectory)
           newSingleReconWorkbook.singleAccountReconcilliationformat()
           newSheet = SpreadsheetDesigner(workbook, tabName, monthlyFolderDirectory)
           newSheet.insertNewAccountBalances(accountAndBalanceDict[workbook])
        else:
            newSingleReconWorkbook = SpreadsheetCreator(workbook, tabName, monthlyFolderDirectory)
            newSingleReconWorkbook.doubleAccountReconcilliationformat()
            newSheet = SpreadsheetDesigner(workbook, tabName, monthlyFolderDirectory)
            newSheet.insertNewAccountBalances(accountAndBalanceDict[workbook])











