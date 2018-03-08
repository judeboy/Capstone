from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from webargs import fields
from flask_apispec import use_kwargs, marshal_with




def create_app:
    app = Flask(__name__)
    return app
    
ma = Marshmallow(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
