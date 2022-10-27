from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField,
                        BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length

class CreateBotForm(FlaskForm):
    name = StringField('Bot Name*', validators=[InputRequired('Give me a name'),
                                    Length(min=1, max=100)])
    description = TextAreaField('Bot Description', 
                                validators=[Length(min=0, max=100)])
    submit = SubmitField('Submit')