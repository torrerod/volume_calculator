from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Volume(FlaskForm):
    diameter= DecimalField(label="Diameter in mm",validators=[DataRequired(message='please enter the diameter in mm')])
    height=DecimalField(label="Cylinder height mm",validators=[DataRequired()])
    submit=SubmitField(label="calculate volume")
