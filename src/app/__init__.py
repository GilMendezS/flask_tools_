from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
toolbar = DebugToolbarExtension(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

from app.users.controllers import mod_auth as auth_module
from app.posts.controllers import mod_post as post_module
app.register_blueprint(auth_module)
app.register_blueprint(post_module)

db.create_all()