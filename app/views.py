# encoding: utf8

user = {'nickname': u'Павел'}

from app import app
from app.forms import LoginForm
from flask import redirect, flash

@app.route('/')
@app.route('/index')
def index():
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


from flask import render_template


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID = ' + form.openid.data +
              ', remember_me: ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title=u'Вход',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
