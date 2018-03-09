import os
# import psycopg2
# DATABASE_URL = os.environ['postgres://localhost/capstone']
# conn = psycopg2.connect(DATABASE_URL, sslmode='postgres://localhost/capstone')

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = os.envron['postgres://localhost/capstone']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
