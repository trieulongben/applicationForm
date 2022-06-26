from flask import Flask,render_template,request,redirect,url_for,session
app = Flask(__name__,template_folder='',static_folder='lib/',)
app.secret_key = 'motconvitxeorahaicaicanh'
import requests
import os
################################################################################

import numpy as np
import pandas as pd 

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
################################################################################


    ################################################################################

#Function 2

################################################################################
#Routes
UPLOAD_FOLDER = 'uploaded/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

keyword1=['python', 'java', 'javascript', 'SQL', 'C++']
keyword2=['SQL', 'java', 'C', 'SQL', 'C++']




def estScore(x,keyword):
    score=0
    #x=x.split(',')
    for i in x:
        if i in keyword:
            score+=1
    return (score/len(keyword))*100



@app.route("/")
def main():
    return "Welcome!"
@app.route("/application", methods=['GET','POST'])
def application():
    return render_template('applicationForm.html',keyword1=keyword1,keyword2=keyword2)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route("/formProcess", methods=['POST'])
def formProcess():
    if request.method == 'POST':
        #Information handle
        #name = request.form['First name'] + request.form['Family name']
        #citizenship=request.form['Citizenship']
       # birth=request.form
        formOut=dict(request.form.lists())
        keyword=[]
        print(formOut['Application for'])
        if 'Data Engineer' in formOut['Application for']:
            keyword=keyword2
        elif 'Data Science' in formOut['Application for']:
            keyword=keyword1
        score=estScore(formOut['acknow'],keyword)
        print(score)
        #Resume Upload handle
        if 'Application letter' not in request.files:
            flash('No file part')
            return 'No file part'
        Applicationletter = request.files['Application letter']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if Applicationletter.filename == '':
            flash('No selected file')
            return 'No selected file'
        if Applicationletter and allowed_file(Applicationletter.filename):
            filename = secure_filename(Applicationletter.filename)
            Applicationletter.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Success'

if __name__ == "__main__":
    app.run(debug=True)