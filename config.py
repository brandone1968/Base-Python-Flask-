import os

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'
LISTINGS_PER_PAGE = 5

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'miodb.sqlite')