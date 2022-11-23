import os

class DevelopmentConfig:
    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(
    #     **{
    #         'user': os.getenv('DB_USER', 'XXX'),
    #         'password': os.getenv('DB_PASSWORD', 'XXX'),
    #         'host': os.getenv('DB_HOST', 'XXX'),
    #         'database': os.getenv('DB_DATABASE', 'app')
    #     }
    # )
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = False

    # os.urandom(24)で生成
    SECRET_KEY = b'g\xebQ\xe9\x1a\xa7\x05z\xb6\xc3\xab\xd8Y\xcc\xd21\xda\xc2\t\\\xd4\xbd0\xf0'

Config = DevelopmentConfig