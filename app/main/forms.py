from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    numPosts = IntegerField('Number of Posts to Query', validators=[DataRequired()])
    keywords = SelectField('Frequency Type', choices=[(0, 'Subreddits'), (1, 'Keywords')]) #should remove popular english words (the, a etc.)
    time = SelectField('Within ', choices=[(0, '24hr'), (1, 'Week'), (2, 'Month'), \
                                                   (3, 'Year'), (4, 'All time')])
    forum = SelectField('From ', choices=[(0, '/r/all'), (1, '/r/popular')])
    submit = SubmitField('Submit')