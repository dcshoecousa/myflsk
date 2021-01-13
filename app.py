from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_session import RedisSessionInterface
from admin import admin
from api import api
from common.RedisHelper import redis_conn
from common.MysqlHelper import db


app = Flask(__name__)
app.config.from_object("settings.DevSettings")

# app.session_interface = RedisSessionInterface(redis=redis_conn, key_prefix='dc')

app.register_blueprint(api)
app.register_blueprint(admin, url_prefix='/admin')

# 自定义script命令
manager = Manager(app)
@manager.option('-n', '--name', dest='name')
@manager.option('-t', '--table', dest='table')
def import_csv(name, table):
    """
    python app.py -n user.csv -t user
    python app.py --name user.csv --t user
    :param name:
    :param table:
    :return:
    """
    print(name, table)

db.init_app(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
