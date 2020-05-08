businessName = "Future Reach Marketing LLC"
bizName = ((businessName.replace(" ","+"))+"_General+Ledger.xlsx")


class IndexMatch:
    def __init__(self, workbook):
        self.workbook = workbook
        self.valuesDict = {} #Will be used to return a {Account Number:Account Value} ex. {200100:25.32}

    def getValues(self):
        #Open spreadsheet.
        from openpyxl import load_workbook
        from openpyxl.utils import get_column_letter
        import os
        os.chdir("/home/doncapodilupo/Downloads")
        wb = load_workbook(filename=self.workbook).active
        total_for_range = wb['A']
        total_amount_range = wb['J']

        #Get all values from column A that are relevant
        for cell in total_for_range:
            cellString = str(cell.value).lstrip(" ")[0:16]
            if "Total for" in cellString:
                self.valuesDict[cellString] = "J"+str(cell.row-1)
        #Get all of the values from column J that are relevant

        for key, correctCell in self.valuesDict.items():
            self.valuesDict[key] = wb[correctCell].value
        return self.valuesDict





#Convert the downloaded file into a CSV. Add headers to make Pandas play nice.






#Search through the GL to figure out which accounts need to be reconned. Returns in the form of a list.
#This skips over accounts that haven't had activity for the date range of the GL.




cat = IndexMatch(bizName)
cat.getValues()