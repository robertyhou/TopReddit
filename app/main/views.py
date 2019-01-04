from flask import render_template
from . import main
from Parser import temp


@main.route('/')
def index():
    temp()
    return render_template('index.html')
