from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class HAR_Form(FlaskForm):
    raw_data = TextAreaField('Raw Data', render_kw={'class': 'form-control', 'rows': 20, 'cols': 85 }, validators=[DataRequired()])
    submit = SubmitField('Classify Acitivty', render_kw={'class': 'btn btn-primary' })