from flask import Flask, session, redirect, url_for, escape
from flask import render_template
from flask import request
from flask import Markup
from flask import make_response
from flask import abort
from flask_bootstrap import Bootstrap
from flask import send_file

import urllib3
import json


app = Flask(__name__)
Bootstrap(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': #this block is only entered when the form is submitted
        response = request.form.get('recaptcha_response')
        name = request.form.get('name')
        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_secret = '6Ld9wpYUAAAAACWUcpl9SCdzmOhw7qJnAFGviuy_'
        http = urllib3.PoolManager()
        r = http.request('GET', recaptcha_url+'?secret='+recaptcha_secret+'&response='+response)
        print(r.data)
        json_data = json.loads(r.data)
        score = json_data['score']
        return render_template('hello.html',score=score,name=name)
    return render_template('hello.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        return send_file('./static/love.png',
            as_attachment=True, attachment_filename='love.png')
    return '''Confirm Download
<form action="/download" method="post">
        <button type="submit" formmethod="post">Click Me!</button>
        </form>'''
