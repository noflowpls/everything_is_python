from distutils.log import debug
import re
from flask import Flask, render_template, url_for, redirect, render_template_string
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('demo.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'test' and password == 'bruteforce_me':
        return render_template_string("Okie")
    else:
        return render_template_string("Nope")

app.run(host='0.0.0.0', port=81, debug=True)