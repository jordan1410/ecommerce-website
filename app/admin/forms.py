from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import InputRequired, Length


class AdminLogin(FlaskForm):

    password = PasswordField('Enter password:', validators=[
                             InputRequired(), Length(max=30)])

    submit = SubmitField("Submit")


class AdminOrders(FlaskForm):

    confirmed = SubmitField('Confirm')

    employee = SubmitField('Employee')

    completed = SubmitField('Complete')

    delete = SubmitField('Delete')
