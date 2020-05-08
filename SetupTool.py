
months = {"01":"JAN",
          "02":"FEB",
          "03":"MAR",
          "04":"APR",
          "05":"MAY",
          "06":"JUN",
          "07":"JUL",
          "08":"AUG",
          "09":"SEP",
          "10":"OCT",
          "11":"NOV",
          "12":"DEC"}


def getSheetTitle():
    import datetime
    current_time = datetime.datetime.now()
    sheetTitle = current_time.strftime('%m%d%y')
    return sheetTitle

def getMonthlyFolderTitle():
    import datetime
    current_time = datetime.datetime.now()
    monthlyFolderTitle = current_time.strftime('%m%y')
    monthlyFolderTitle = months[monthlyFolderTitle[0:2]]+monthlyFolderTitle[2:]
    return monthlyFolderTitle


def directorySetup():  # This will ensure that all required files and directories are present before continuing.
    import os
    print("Initializing setup.\n")
    # Create directories
    neededDirectories = ['Recons']
    for i in neededDirectories:
        try:
            # Create target Directory
            print(os.getcwd())
            os.mkdir(i)
            print("Directory " + i + " Created ")
        except FileExistsError:
            print("Directory " + i + " already exists")
        os.chdir(i)
        try:
            os.mkdir(getMonthlyFolderTitle())
            print("The monthly folder "+getMonthlyFolderTitle()+ " has been created.")
        except FileExistsError:
            print("The monthly folder " + getMonthlyFolderTitle() + " already exists.")
    print("All directories are present.\n")


directorySetup()