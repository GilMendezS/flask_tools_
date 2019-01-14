from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'secretehere'
bcrypt = Bcrypt(app)

password_gms = 'sgms'
hashed = bcrypt.generate_password_hash(password_gms)
print(hashed)
matched_password = bcrypt.check_password_hash(hashed, password_gms)
print(matched_password)
app.run(debug = True)