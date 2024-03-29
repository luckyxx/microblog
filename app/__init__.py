
from flask import Flask#从flask包中导入Flask类
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

from flask_login import LoginManager

from logging.handlers import RotatingFileHandler
import os
import logging


app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)
login = LoginManager(app)
login.login_view='login'  # ''里的login  是route .py 里的login函数名

if not app.debug:

    db = SQLAlchemy(app)#数据库对象
    migrate = Migrate(app, db)#迁移引擎对象
    print('等会谁（哪个包或模块）在使用我：',__name__)
    if not os .path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
from app import routes,models,errors#从app包中导入模块routes


