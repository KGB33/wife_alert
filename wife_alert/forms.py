from flask_wtf import FlaskForm
from wtforms import SubmitField


class ButtonForm(FlaskForm):
    submit = SubmitField("Make Blink")
