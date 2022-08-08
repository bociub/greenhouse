from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.greenHouse import GreenHouse, greenHouse_list

from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional

class GreenHouseListResource(Resource):

    def get(self):

        greenHouses = GreenHouse.get_all_forSale()

        data = []

        for greenHouse in greenHouses:
            data.append(greenHouse.data())

        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):
        json_data = request.get_json()

        current_user = get_jwt_identity()

        """greenHouse = GreenHouse(name=json_data['name'],
                        description=json_data['description'],
                        num_of_servings=json_data['num_of_servings'],
                        cook_time=json_data['cook_time'],
                        directions=json_data['directions'],
                        user_id=current_user)"""
    
        greenHouse = GreenHouse(name = json_data['name'],
        plant = json_data['plant'],
        postcode = json_data['postcode'],
        plantingDate = json_data['plantingDate'],
        forSale = json_data['forSale'],
        bookedForSale = json_data['bookedForSale'],
        energyPlan = json_data['energyPlan'],
        harvestDate = json_data['harvestDate'],
        counterForAVG = json_data['counterForAVG'],
        AVGofAirTemperature = json_data['AVGofAirTemperature'],
        GivenDaysWeather = json_data['GivenDaysWeather'],
        currentParameters = json_data['currentParameters'],
        user_id=current_user)
    

        greenHouse.save()

        return greenHouse.data(), HTTPStatus.CREATED


class GreenHouseResource(Resource):

    @jwt_optional
    def get(self, greenHouse_id):

        greenHouse = GreenHouse.get_by_id(greenHouse_id=greenHouse_id)

        if greenHouse is None:
            return {'message': 'GreenHouse not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        """Authorization?"""

        if greenHouse.forSale == False and greenHouse.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return greenHouse.data(), HTTPStatus.OK

    @jwt_required
    def put(self, greenHouse_id):

        json_data = request.get_json()

        greenHouse = GreenHouse.get_by_id(greenHouse_id=greenHouse_id)

        if greenHouse is None:
            return {'message': 'GreenHouse not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != greenHouse.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN


        greenHouse.name = json_data['name']
        greenHouse.plant = json_data['plant']
        greenHouse.postcode = json_data['postcode']
        greenHouse.plantingDate = json_data['plantingDate']
        greenHouse.forSale = json_data['forSale']
        greenHouse.bookedForSale = json_data['bookedForSale']
        greenHouse.energyPlan = json_data['energyPlan']
        greenHouse.harvestDate = json_data['harvestDate']
        greenHouse.counterForAVG = json_data['counterForAVG']
        greenHouse.AVGofAirTemperature = json_data['AVGofAirTemperature']
        greenHouse.GivenDaysWeather = json_data['GivenDaysWeather']
        greenHouse.currentParameters = json_data['currentParameters']
        
        

        greenHouse.save()

        return greenHouse.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, greenHouse_id):

        greenHouse = GreenHouse.get_by_id(greenHouse_id=greenHouse_id)

        if greenHouse is None:
            return {'message': 'GreenHouse not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != greenHouse.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        greenHouse.delete()

        return {}, HTTPStatus.NO_CONTENT


class GreenHousePublishResource(Resource):

    def put(self, greenHouse_id):
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.forSale = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, greenHouse_id):
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.forSale = False

        return {}, HTTPStatus.NO_CONTENT













"""without db
class GreenHouseListResource(Resource):
    
    

    def get(self):

        data = []

        for greenHouse in greenHouse_list:
            if greenHouse.forSale is True:
                data.append(greenHouse.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        greenHouse = GreenHouse(name=data['name'],
                                plant=data['plant'],
                                postcode=data['postcode'])



        greenHouse_list.append(greenHouse)

        return greenHouse.data, HTTPStatus.CREATED #jsonfy omitted because of inherited Resource did it
    
class GreenHouseResource(Resource):

    def get(self, greenHouse_id):
        #return {'holly duck'}, HTTPStatus.NOT_FOUND
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id and greenHouse.forSale == True), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        return greenHouse.data, HTTPStatus.OK

    def put(self, greenHouse_id): #overwrites
        data = request.get_json()

        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.name = data['name']
        greenHouse.plant = data['plant']
        greenHouse.postcode = data['postcode']
        greenHouse.forSale = data['forSale']


        return greenHouse.data, HTTPStatus.OK


class GreenHousePublishResource(Resource):

    def put(self, greenHouse_id):
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.forSale = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, greenHouse_id): #for_sale goes to false - no deleting
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.forSale = False

        return {}, HTTPStatus.NO_CONTENT"""

