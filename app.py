from flask import Flask, render_template, request,url_for,redirect
from werkzeug.utils import secure_filename
import os

import SetupTool
SetupTool.directorySetup()

ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'Upload Folder'
ALLOWED_EXTENSIONS = {'xlsx'}




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/', methods=["POST","GET"])
def main_Menu():
    if request.method == "POST":
        if request.form['btn_Confirm'] == 'Go To Recon Page':
            return redirect(url_for('recon_Window'))
    else:
        return render_template('main.html')





accounts_That_Need_Recons_Created = []
data = []

@app.route('/ReconWindow', methods=["POST","GET"])
def recon_Window():
    if request.method == 'POST':

        uploaded_file = request.files['excel_file']

        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            from BackEndLogic import accountsInGeneralLedger, accountsInDirectory, Recon

            accounts_In_GL = accountsInGeneralLedger(filename)
            accounts_In_Directory = accountsInDirectory()

            #fills out data and accounts_That_Need_Recons_Created
            for account in accounts_In_GL.keys():
                os.chdir(ROOT)
                temp_name = account+".xlsx"
                if temp_name in accounts_In_Directory:
                    data.append(Recon(account, accounts_In_GL[account], True))
                elif account not in accounts_In_Directory:
                    data.append(Recon(account, accounts_In_GL[account],False))
                    accounts_That_Need_Recons_Created.append(Recon(account, accounts_In_GL[account],False))

                else:
                    data.append(Recon(account, accounts_In_GL[account], False))

        return render_template('ReconWindow.html', data=data)


    elif request.method == "GET":
        return render_template("ReconWindow.html")


@app.route('/SingleRecon', methods=["POST","GET"])
def create_Recon_Single():
    if request.method == 'POST':
        for account in accounts_That_Need_Recons_Created:
            os.chdir(ROOT)

            if request.form['Single_Recon'] == "Assign Single Reconciliation " + account.account_Name:
                from Classes.SpreadsheetCreator import SpreadsheetCreator
                from BackEndLogic import Recon
                recon = SpreadsheetCreator(account.account_Name + ".xlsx")
                recon.singleAccountReconcilliationformat(account.account_Balance)
                new_Recon_Obj = Recon(account.account_Name, account.account_Balance, True)
                for index, obj in enumerate(data):
                    if obj.account_Name == account.account_Name:
                        del data[index]

                data.append(new_Recon_Obj)
            accounts_That_Need_Recons_Created.remove(account)

            return render_template('ReconWindow.html', data=data)


    else:
        return render_template('ReconWindow.html', data=data)


@app.route('/DoubleRecon', methods=["POST","GET"])
def create_Recon_Double():
    if request.method == 'POST':
        for account in accounts_That_Need_Recons_Created:
            os.chdir(ROOT)

            if request.form['Double_Recon'] == "Assign Double Reconciliation " + account.account_Name:
                from Classes.SpreadsheetCreator import SpreadsheetCreator
                from BackEndLogic import Recon
                recon = SpreadsheetCreator(account.account_Name + ".xlsx")
                recon.doubleAccountReconcilliationformat(account.account_Balance)
                new_Recon_Obj = Recon(account.account_Name,account.account_Balance,True)
                for index, obj in enumerate(data):
                    if obj.account_Name == account.account_Name:
                        del data[index]


                data.append(new_Recon_Obj)
            accounts_That_Need_Recons_Created.remove(account)
        return render_template('ReconWindow.html', data=data)
    else:
        return render_template('ReconWindow.html', data=data)


if __name__ == '__main__':
    app.run()
