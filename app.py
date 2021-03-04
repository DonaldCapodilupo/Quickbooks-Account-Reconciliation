# tkinter is used for the user interface
import tkinter as tk
# custom classes made to create good looking buttons and entries
from class_buttons import Button
from class_entry import Entry
from tkinter.filedialog import askopenfile
import SetupTool
import os
from os import path
ROOT = path.dirname(path.realpath(__file__))
SetupTool.directorySetup()
os.chdir(ROOT)


# this is the class called when the program starts
# it inherits a tkinter window
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # basic config
        # tk.Tk.wm_geometry(self, '1280x720')
        tk.Tk.wm_resizable(self, True, True)
        tk.Tk.wm_title(self, 'Online Giveaway Solutions')
        tk.Tk.config(self, bg='#333333')  # hex color #333333 is dark gray
        # create variable
        self.current_frame = None
        # set home frame
        self.switch_frame(MainMenu)


    # this function switches the current frame for the frame entered
    def switch_frame(self, frame):
        try:
            self.current_frame.destroy()
        except:
            pass
        self.current_frame = frame(self)
        self.current_frame.pack()


class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg='#333333')

        lbl_Company_Name = tk.Label(self, text='Account Reconciliation Software', font=('Arial', 25, 'bold'), bg='#333333', fg='#ffffff')
        lbl_Company_Name.grid(row=0,column=2)

        tk.Label(self, bg='#333333', fg='#ffffff').grid(row=1,column=1,pady=50)

        # using custom buttons for the ui
        btn_Start_Program = Button(root=self, text='Begin Reconciliation', command=lambda x: master.switch_frame(ReconWindow))
        btn_Start_Program.grid(row=2,column=2)


        btn_Exit_App = Button(root=self, text='Exit', command=lambda x: master.destroy())
        btn_Exit_App.grid(row=10,column=2)


class ReconWindow(tk.Frame):
    def __init__(self, master):
        import os
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg='#333333')
        tk.Label(self, bg='#333333').grid(row=0,column=1)  # spacing

        btn_Select_File = Button(root=self, text='Select A File',
                             command=lambda x: getDownloadedFile())
        btn_Select_File.grid(row=1, column=0)


        lbl_File_Name = tk.Label(self, text='FILE NAME WILL APPEAR HERE')
        lbl_File_Name.grid(row=1, column=1)


        btn_Confirm = Button(root=self, text='Begin Reconciliation',
            command=lambda x: confirmButton())
        btn_Confirm.grid(row=2, column=1)



        def getDownloadedFile():
            user_File = askopenfile(parent=master, mode='rb', title="Choose a file", filetype=[("XLSX file", "*.xlsx",)]).name
            lbl_File_Name.config(text=user_File)

        def confirmButton():
            from BackEndLogic import accountsInGeneralLedger, accountsInDirectory

            accounts_In_GL = accountsInGeneralLedger(lbl_File_Name.cget("text")) #Dict {Account Name:$0.00}
            accounts_In_Directory = accountsInDirectory() #List

            results_text_box = tk.Text(self, height=30, width=100)

            for key in accounts_In_GL.keys():
                key = key+".xlsx"
                if key in accounts_In_Directory:
                    results_text_box.insert(1.0, key + " is in the directory. Updating...\n")
                    results_text_box.tag_configure("center", justify="center")
                    results_text_box.tag_add("center", 1.0, "end")
                    results_text_box.grid(column=0, row=5, columnspan=5)
                    from Classes.SpreadsheetDesigns import SpreadsheetDesigner
                    from SetupTool import getMonthlyFolderTitle
                    new_worksheet = SpreadsheetDesigner(key,getMonthlyFolderTitle(),"Recons/"+getMonthlyFolderTitle())
                    new_worksheet.moveAndCopyWorksheet()
                    new_worksheet.insertNewAccountBalances(accounts_In_GL[key[:-5]])

                else:
                    results_text_box.insert(1.0, key + " is not in the directory and needs to be created.\n")
                    results_text_box.tag_configure("center", justify="center")
                    results_text_box.tag_add("center", 1.0, "end")
                    results_text_box.grid(column=0, row=5, columnspan=5)



class AddRecon(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg='#333333')

        lbl_Company_Name = tk.Label(self, text='Account Reconciliation Software', font=('Arial', 25, 'bold'), bg='#333333', fg='#ffffff')
        lbl_Company_Name.grid(row=0,column=2)

        tk.Label(self, bg='#333333', fg='#ffffff').grid(row=1,column=1,pady=50)

        # using custom buttons for the ui
        btn_Start_Program = Button(root=self, text='Begin Reconciliation', command=lambda x: master.switch_frame(ReconWindow))
        btn_Start_Program.grid(row=2,column=2)


        btn_Exit_App = Button(root=self, text='Exit', command=lambda x: master.destroy())
        btn_Exit_App.grid(row=10,column=2)


if __name__ == '__main__':
    window = Main()
    window.mainloop()
