from flask import Flask, render_template
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db, jwt
from resources.user import UserListResource, UserResource, MeResource
from resources.token import TokenResource, RefreshResource, TokenResource2
#from models.user import User
from resources.greenHouse import GreenHouseListResource, GreenHouseResource, GreenHousePublishResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

def register_resources(app):
    api = Api(app)    

    api.add_resource(TokenResource2, '/')
  

if __name__ == '__main__':
    app = create_app()
    app.run(port=80, debug=True)
    
    