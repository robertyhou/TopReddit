from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

"""
The form displayed on the home page. Contains several fields to allow for user customized queries.
The key values of the fields can be directly inputted into the Parser class, and Reddit API,
to query data from Reddit. 
"""
class QueryForm(FlaskForm):
    numPosts = IntegerField('Number of Posts to Query', \
                            validators=[DataRequired(), \
                                        NumberRange(min=1, max=1000, message='Must query between 1 and 1000 posts')])
    time = SelectField('Within ', choices=[('day', '24hr'), ('week', 'Week'), ('month', 'Month'), \
                                                   ('year', 'Year'), ('3', 'All time')])
    forum = SelectField('From ', choices=[('all', '/r/all'), ('popular', '/r/popular')])
    submit = SubmitField('Submit')
