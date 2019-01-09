from flask import Blueprint

main = Blueprint('main', __name__)

#At bottom to prevent cyclic import
from . import views
