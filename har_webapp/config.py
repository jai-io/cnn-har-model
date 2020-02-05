import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'd41d8cd98f00b204e9800998ecf8427e'