from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_apispec import use_kwargs, marshal_with
from flask_marshmallow import Marshmallow
from webargs import fields


app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
ma = Marshmallow(app)
migrate = Migrate(app, db)




from app import routes, models
