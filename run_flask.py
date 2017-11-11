#!/usr/bin/env python3

# -*- coding:utf-8 -*-


from flask import Flask, url_for, render_template
from flask_jsonrpc import JSONRPC
app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@app.route('/')
def hello():
    name = {'a':1, 'b':2} 
    return render_template('hello.html', name=name)

@jsonrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'
@app.route('/san/<username>')
def txt(username):
    return username


with app.test_request_context():
    print(url_for('txt', username='tyan'))

if __name__ == '__main__':
    app.run(debug=True)

