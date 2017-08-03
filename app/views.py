from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app

__author__ = 'haoSev'


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'nickname': 'haoran'},
            'body': 'That is amazing!'
        },
        {
            'author': {'nickname': 'pengfei'},
            'body': 'That is crazy!'
        }
    ]
    return render_template('index.html',
                           posts=posts,)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
              '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
