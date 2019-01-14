from wtforms import Form, TextField, PasswordField, BooleanField, validators

class PostForm(Form):
    title = TextField('Title', [validators.Required()])
    description = TextField('Description', [validators.Required()])
