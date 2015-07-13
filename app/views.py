# encoding: utf8

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': u'Павел'}
    posts = [
        {
            'author': {'nickname': u'Люк'},
            'body': u'Использование силы'
        },
        {
            'author': {'nickname': u'Лея'},
            'body': u'Политические вопросы'
        }
    ]
    return render_template('index.html', user=user, posts=posts)