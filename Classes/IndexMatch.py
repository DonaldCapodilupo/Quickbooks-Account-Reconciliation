class IndexMatch:
    def __init__(self, workbook):
        self.workbook = workbook
        self.valuesDict = {} #Will be used to return a {Account Number:Account Value} ex. {200100:25.32}

    def getValues(self):
        #Open spreadsheet.
        from openpyxl import load_workbook
        import os
        os.chdir("/home/doncapodilupo/Downloads")
        wb = load_workbook(filename=self.workbook).active
        total_for_range = wb['A']

        #Get a dict that follows this format: {"Total For ...":THE CORRECT ADJACENT CELL}
        for cell in total_for_range:
            cellString = str(cell.value).lstrip(" ")+".xlsx"
            correctFormat = cellString.replace("/","") #Throws error if file name has something like "(A/R)" in it
            if "Total for" in correctFormat:
                self.valuesDict[correctFormat] = "J"+str(cell.row-1)

        # Get a dict that follows this format: {"Total For ...":"$125.63"}
        for key, correctCell in self.valuesDict.items():
            self.valuesDict[key] = wb[correctCell].value
        return self.valuesDict



