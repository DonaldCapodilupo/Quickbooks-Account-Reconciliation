from os import path



businessName = "Future Reach Marketing LLC"
bizName = ((businessName.replace(" ","+"))+"_General+Ledger.xlsx")




ROOT = path.dirname(path.realpath(__file__))
print(ROOT)



if __name__ == "__main__":
    print("Hello and welcome to the accounting reconciliation software V0.01")
    print("Created by Donald Capodilupo")
    from Classes.DirectoryManipulator import DirectoryManipulator
    from Classes.IndexMatch import IndexMatch
    confirmDownload = DirectoryManipulator("/home/doncapodilupo/Downloads")
    confirmDownload.checkDownload()
    accountAndBalanceDict = IndexMatch(bizName).getValues()
    print(accountAndBalanceDict)

