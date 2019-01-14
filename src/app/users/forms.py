from wtforms import Form, TextField, PasswordField, BooleanField, validators

class LoginForm(Form):
    email = TextField('Email Address',[validators.Email(),validators.Required(message="Forgot your email adddress?")])
    password = PasswordField('Password', [validators.Required(message='Must provide a password')])

