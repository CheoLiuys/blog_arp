#-*- coding:utf-8 -*-
# author:刘超
# datetime:2019/9/29 13:25
# software: PyCharm
# TEL:17854169557
from run import app
from flask import render_template

@app.route('/')
def index():
    '''
    首页
    :return:
    '''
    return render_template('index.html')

@app.route('/admin')
def admin_index():
    '''
    后台管理首页
    :return:
    '''
    return render_template('admin_index.html')

@app.route('/admin_article')
def admin_article():
    '''
    后台管理文章页
    :return:
    '''
    return render_template('admin_article.html')

@app.route('/category')
def category():
    '''
    文章分类页
    :return:
    '''
    return render_template('category.html')

@app.route('/user')
def user():
    '''
    用户页
    :return:
    '''
    return render_template('user.html')