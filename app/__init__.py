from flask import Flask
# , jsonify
from config import Config

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
# from webargs import fields
# from flask_apispec import use_kwargs, marshal_with
#
#
app = Flask(__name__)
app.config.from_object(Config)

# db = SQLAlchemy(app)
# ma = Marshmallow(app)
# migrate = Migrate(app, db)
#
#
#
#
from app import routes

# , models
