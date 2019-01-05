from flask import render_template
from . import main
from Parser import temp
from .forms import QueryForm

@main.route('/')
def index():
    form = QueryForm()
    if form.validate_on_submit():
        print(5)
    temp()
    return render_template('index.html', form=form)
