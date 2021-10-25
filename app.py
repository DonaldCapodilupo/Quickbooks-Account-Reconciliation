from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

import SetupTool

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["POST", "GET"])
def main_Menu():
    if request.method == 'POST' and request.form.get("TheButton"):
        print(request.form.getlist('TheButton'))
        print(os.getcwd())



        uploaded_file = request.files['excel_file']
        filename = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        from BackEndLogic import accountsInGeneralLedger, accountsInDirectory, Recon
        accounts_In_GL = accountsInGeneralLedger(filename)
        accounts_In_Directory = accountsInDirectory()

        # fills out data and accounts_That_Need_Recons_Created
        for account in accounts_In_GL.keys():
            temp_name = account + ".xlsx"
            if temp_name in accounts_In_Directory:
                data.append(Recon(account, accounts_In_GL[account], True))
            elif account not in accounts_In_Directory:
                data.append(Recon(account, accounts_In_GL[account], False))
                accounts_That_Need_Recons_Created.append(Recon(account, accounts_In_GL[account], False))
            else:
                data.append(Recon(account, accounts_In_GL[account], False))
        return render_template('main.html', data=data)

    elif request.method == 'POST' and request.form.get("Single_Recon"):
        print(request.form.get("Single_Recon")[-5:])
        for account in accounts_That_Need_Recons_Created:
            if request.form.get("Single_Recon")[-5:] in account.account_Name:

                from Classes.SpreadsheetCreator import SpreadsheetCreator
                from BackEndLogic import Recon
                recon = SpreadsheetCreator(account.account_Name + ".xlsx")
                recon.singleAccountReconciliationFormat(account.account_Balance)
                new_Recon_Obj = Recon(account.account_Name, account.account_Balance, True)
                for index, obj in enumerate(data):
                    if obj.account_Name == account.account_Name:
                        del data[index]
                data.append(new_Recon_Obj)
                accounts_That_Need_Recons_Created.remove(account)
                return render_template('main.html', data=data)

    elif request.method == 'POST' and request.form["Double_Recon"]:
        print(request.form.get("Double_Recon")[-5:])
        for account in accounts_That_Need_Recons_Created:
            if request.form.get("Double_Recon")[-5:] in account.account_Name:

            # if request.form['Double_Recon'] == "Assign Double Reconciliation " + account.account_Name:
                from Classes.SpreadsheetCreator import SpreadsheetCreator
                from BackEndLogic import Recon
                recon = SpreadsheetCreator(account.account_Name + ".xlsx")
                recon.doubleAccountReconciliationFormat(account.account_Balance)
                new_Recon_Obj = Recon(account.account_Name, account.account_Balance, True)
                for index, obj in enumerate(data):
                    if obj.account_Name == account.account_Name:
                        del data[index]
                data.append(new_Recon_Obj)
                accounts_That_Need_Recons_Created.remove(account)
                return render_template('main.html', data=data)



    elif request.method == "GET":
        return render_template("main.html", data=False)


# These lists need to persist between web pages.




if __name__ == '__main__':
    port = 5420
    url = "http://127.0.0.1:{0}".format(port)


    #threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    SetupTool.directorySetup()
    accounts_That_Need_Recons_Created = []
    data = []

    app.config['UPLOAD_FOLDER'] = 'Upload Folder'
    ALLOWED_EXTENSIONS = {'xlsx'}

    app.run(port=port, debug=False)
