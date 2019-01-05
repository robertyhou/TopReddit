from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    numPosts = StringField('Number of posts to Query', validators=[DataRequired()])
    submit = SubmitField('Submit')