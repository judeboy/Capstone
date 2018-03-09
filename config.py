import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://desyrgytwnqqsz:b0fbf3976ab15ee0e05844a889459d0e4fefe2be0cf1ee1e8a2ed12f02d992b9@ec2-54-235-66-24.compute-1.amazonaws.com:5432/d5bmadat7p5o27') or \
        'postgres://localhost/capstone'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
