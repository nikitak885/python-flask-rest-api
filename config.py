import os

# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@db/users')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@db/users')
SQLALCHEMY_TRACK_MODIFICATIONS = False
