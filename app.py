from flask import Flask
from flask_restful import Api

from resources.greenHouse import GreenHouseListResource, GreenHouseResource, GreenHousePublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(GreenHouseListResource, '/recipes')
api.add_resource(GreenHouseResource, '/recipes/<int:recipe_id>')
api.add_resource(GreenHousePublishResource, '/recipes/<int:recipe_id>/publish')

@app.route("/")###########notneeded#####
def hello():###########notneeded#####
    return "running"###########notneeded#####

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
exercise 10 next
