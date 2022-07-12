from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from chessassist.config import Config

#extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'

#app factory
def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from chessassist.main.routes import main
    from chessassist.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app