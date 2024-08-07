from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'lightbridge'

  from .view import view
  app.register_blueprint(view, url_prefix='/')

  from .auth import auth
  app.register_blueprint(auth, url_prefix='/')

  return app