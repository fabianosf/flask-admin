import os

class Config:
    FLASK_ADMIN_SWATCH = 'cosmo'
    SECRET_KEY = 'SECRET' 
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['DATABASE_TRACK_MODIFICATIONS']
