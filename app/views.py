from flask import render_template

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