from flask import Flask, render_template, request,url_for,redirect
from werkzeug.utils import secure_filename
import os

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
        return redirect(url_for('main_Menu'))

    elif request.method == "GET":
        return render_template("ReconWindow.html")









if __name__ == '__main__':
    app.run()
