from flask import render_template, flash, redirect, url_for
from . import main
from Parser import Parser
from .forms import QueryForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        parser = Parser(int(form.numPosts.data), form.forum.data, form.time.data)
        parser.plot()
        return render_template('index.html', form=form)
        #return redirect(url_for('main.index'))
    parser = Parser()
    parser.plot()
    return render_template('index.html', form=form)
