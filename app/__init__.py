from flask import Flask
from config import Config

# import our blueprints for registration
from .blog.routes import blog
from .auth.routes import auth

from .models import db
# import database related
from flask_migrate import Migrate

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(blog)
app.register_blueprint(auth)

app.config.from_object(Config)

# initialize our databse to work with our app
db.init_app(app)
login.init_app(app)

migrate = Migrate(app, db)

from . import models
from . import routes
