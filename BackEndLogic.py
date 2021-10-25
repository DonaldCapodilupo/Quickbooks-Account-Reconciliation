import pandas as pd
import os

class Recon:
    def __init__(self,account_Name, account_Balance, account_Status_Exists):
        self.account_Name = account_Name
        self.account_Balance = account_Balance
        self.account_Status_Exists = account_Status_Exists

#Returns a dict of all accounts, and their balances, that are located in the GL file. {Account : $0.00}
def accountsInGeneralLedger(fileName):

    accounts_In_General_Ledger = {}

    os.chdir("Upload Folder")

    dataframe = pd.read_excel(fileName, 0, header=4, names=["Title","Date","Account #","Num","Adj","Name","Memo",
                                                            "Debit", "Credit","Balance"])

    dataframe["Balance"] = dataframe["Balance"].fillna(0)


    for index, row in dataframe.iterrows():
        try:
            if "Total for " in row.Title:
                accounts_In_General_Ledger[row.Title.lstrip()[10:].replace("/","")] = raw_Num_To_Currency(dataframe["Balance"].iloc[index-1])
        except TypeError:
            pass
    os.chdir("..")

    #This will convert to a tuple if needed.
    #accounts_In_General_Ledger = [(account_name,account_value) for account_value, account_name in accounts_In_General_Ledger.items()]

    return accounts_In_General_Ledger

#Returns a list of all of the recons currently in the directory
def accountsInDirectory():
    import os
    from SetupTool import getMonthlyFolderTitle
    return os.listdir("Recons/"+getMonthlyFolderTitle())


def raw_Num_To_Currency(raw_Number):
    return "${:,.2f}".format(raw_Number)


