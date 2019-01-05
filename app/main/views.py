from flask import render_template
from . import main
from Parser import Parser
from .forms import QueryForm

"""
Currently the only route for the main page. Must take 'POST'
requests so form data can be accessed. On form submission, 
passes in form data to Parser function and generates new plot.
Updated index.html with new graph displayed. 
"""
@main.route('/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        parser = Parser(int(form.numPosts.data), form.forum.data, form.time.data)
        parser.plot()
        return render_template('index.html', form=form)
    parser = Parser()
    parser.plot()
    return render_template('index.html', form=form)
