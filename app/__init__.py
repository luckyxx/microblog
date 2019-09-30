
from flask import Flask#从flask包中导入Flask

from flask_bootstrap import Bootstrap

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

from config import Config

from logging.handlers import RotatingFileHandler

import os

import logging

from flask_login import LoginManager

from flask_mail import Mail

from flask_moment import Moment

from flask_babel import Babel

from flask import request

from flask_babel import Babel,lazy_gettext as _l

import os
import click


app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)
login = LoginManager(app)
login.login_view='login'  # ''里的login  是route .py 里的login函数名
login.login_message = _l('Please log in to access this page.')

mail=Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)




if not app.debug:

    db = SQLAlchemy(app)#数据库对象
    migrate = Migrate(app, db)#迁移引擎对象
    # print('等会谁（哪个包或模块）在使用我：',__name__)
    if not os .path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info(_l('Microblog startup'))

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return 'zh_cn'



@app.cli.group()
def translate():
    #翻译和本地化命令
    pass

@translate.command()
@click.argument('lang')
def init(lang):
    #初始化一个新语言
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel init -i messages.pot -d app/translations -l ' +lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')
from app import routes,models,errors#从app包中导入模块routes


