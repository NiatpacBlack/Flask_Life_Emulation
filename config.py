import os


class Config(object):
    """ Ключ задается либо в переменной окружения либо непосредственно """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any_key'
