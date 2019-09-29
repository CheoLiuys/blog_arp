#-*- coding:utf-8 -*-
# author:刘超
# datetime:2019/9/29 13:25
# software: PyCharm
# TEL:17854169557
from run import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
