#!/usr/bin/env python3

# -*- coding:utf-8 -*-

import os
from flask import Flask, url_for, render_template, request, redirect
from flask_jsonrpc import JSONRPC
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/churen/work'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
jsonrpc = JSONRPC(app, '/api')

@app.route('/')
def hello():
    name = {'a':1, 'b':2} 
    return render_template('hello.html', name=name)

@jsonrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'
@app.route('/san/<username>')
def txt():
    return username
                
def allowed_file(filename):
    return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/up', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print('hello')
        file_ = request.files['file']
        print('的到了 file')
        if file_ and allowed_file(file_.filename):
            filename = secure_filename(file_.filename)
            print('存开x')
            file_.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('33232')
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
            <!doctype html>
                                                                                                                        <title>Upload new File</title>
                                                                                                                            <h1>Upload new File</h1>
                                                                                                                                <form action="" method=post enctype=multipart/form-data>
                                                                                                                                      <p><input type=file name=file>
                                                                                                                                               <input type=submit value=Upload>
                                                                                                                                                   </form>
                                                                                                                                                       '''
with app.test_request_context():
    print(url_for('txt', username='tyan'))

if __name__ == '__main__':
    app.run(debug=True)

