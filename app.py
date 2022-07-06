from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db
from resources.user import UserListResource
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

def register_resources(app):
    api = Api(app)    
    api.add_resource(GreenHouseListResource, '/greenHouseS')
    api.add_resource(UserListResource, '/users')
    api.add_resource(GreenHouseResource, '/greenHouseS/<int:greenHouse_id>') #for overwritting
    api.add_resource(GreenHousePublishResource, '/greenHouseS/<int:greenHouse_id>/duck') #if delete then forSale=False if put then True


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
    
    



