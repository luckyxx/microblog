import os

basedir = os.path.abspath(os.path.dirname(__file__))#获取当前.py文件的绝对路径


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['mxiaoxuan9988@163.com']
    POSTS_PER_PAGE = 2
    LANGUAGES = ['en', 'zh']#注意：不要填写zh_CN。有坑！

