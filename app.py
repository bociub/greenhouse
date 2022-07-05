from flask import Flask
from flask_restful import Api

from resources.greenHouse import GreenHouseListResource, GreenHouseResource, GreenHousePublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(GreenHouseListResource, '/greenHouseS')
api.add_resource(GreenHouseResource, '/greenHouseS/<int:greenHouse_id>') #for overwritting
api.add_resource(GreenHousePublishResource, '/greenHouseS/<int:greenHouse_id>/duck') #if delete then forSale=False if put then True

@app.route("/")###########notneeded#####
def hello():###########notneeded#####
    return "running"###########notneeded#####

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    



