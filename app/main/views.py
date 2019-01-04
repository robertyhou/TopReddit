from flask import render_template
from . import main
import parser


@main.route('/')
def index():
    parser.temp()
    return render_template('index.html')
