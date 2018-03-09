import os
import psycopg2

basedir = os.path.abspath(os.path.dirname(__file__))
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/capstone'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
