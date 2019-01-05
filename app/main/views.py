from flask import render_template
from . import main
from Parser import temp
from .forms import QueryForm

@main.route('/')
def index():
    form = QueryForm()
    temp()
    return render_template('index.html', form=form)
