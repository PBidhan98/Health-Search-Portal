from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    str = StringField('Query')
    submit = SubmitField('Search')

