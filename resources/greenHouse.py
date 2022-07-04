from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.greenHouse import GreenHouse, greenHouse_list


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
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id and greenHouse.is_publish == True), None)

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


        return greenHouse.data, HTTPStatus.OK


class GreenHousePublishResource(Resource):

    def put(self, greenHouse_id):
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, greenHouse_id): #for_sale goes to false - no deleting
        greenHouse = next((greenHouse for greenHouse in greenHouse_list if greenHouse.id == greenHouse_id), None)

        if greenHouse is None:
            return {'message': 'greenHouse not found'}, HTTPStatus.NOT_FOUND

        greenHouse.is_publish = False

        return {}, HTTPStatus.NO_CONTENT

