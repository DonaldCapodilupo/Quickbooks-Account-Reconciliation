
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
    ROOT = os.path.dirname(os.path.realpath(__file__))
    neededDirectories = ['Recons', 'Upload Folder']
    for directory in neededDirectories:
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

        if directory == "Recons":
            os.chdir('Recons')
            #Make a folder for the current month if one is not created.
            try:
                os.mkdir(getMonthlyFolderTitle())
            except FileExistsError:
                pass
        os.chdir(ROOT)


