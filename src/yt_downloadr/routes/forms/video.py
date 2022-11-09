'''
    Classes
    -------
    SimpleVideoForm(flask_wtf.FlaskForm)
        simple from received in /video post
'''

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class SimpleVideoForm(FlaskForm):
    '''Simple form received in /video post'''
    format_id = StringField('format_id', validators=[DataRequired()])
