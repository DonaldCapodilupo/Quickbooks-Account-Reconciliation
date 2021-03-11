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

            data =[]


            for account in accounts_In_GL.keys():
                os.chdir(ROOT)
                temp_name = account+".xlsx"
                if temp_name in accounts_In_Directory:
                    data.append(Recon(account, accounts_In_GL[account], True))
                    from Classes.SpreadsheetDesigns import SpreadsheetDesigner
                    recon = SpreadsheetDesigner(temp_name)
                    recon.moveAndCopyWorksheet()
                    recon.insertNewAccountBalances(accounts_In_GL[account])

                elif account not in accounts_In_Directory:
                    data.append(Recon(account, accounts_In_GL[account],False))
                    from Classes.SpreadsheetCreator import SpreadsheetCreator
                    recon = SpreadsheetCreator(temp_name)
                    recon.doubleAccountReconcilliationformat(accounts_In_GL[account])


                else:
                    data.append(Recon(account, accounts_In_GL[account], False))

            return render_template('ReconWindow.html', data=data)
                








    elif request.method == "GET":
        return render_template("ReconWindow.html")









if __name__ == '__main__':
    app.run()
