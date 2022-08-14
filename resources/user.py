from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import jwt_optional, get_jwt_identity, jwt_required

from utils import hash_password
from models.user import User


class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')


        if User.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)

        user = User(
            username=username,
            email=email,
            password=password,

        )

        user.save()

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return data, HTTPStatus.CREATED

class UserResource(Resource):

    @jwt_optional
    def get(self, username):

        user = User.get_by_username(username=username)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user == user.id:
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }

        else:
            data = {
                'id': user.id,
                'username': user.username,
            }

        return data, HTTPStatus.OK
        
        
class MeResource(Resource):

    @jwt_required
    def get(self):
        user = User.get_by_id(user_id=get_jwt_identity())
 
        data = {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email
        }
        

        return data, HTTPStatus.OK
    
    @jwt_required    
    def put(self): # variables must be in syncron in the received data and here. if not then nothing happens.

        update_data = request.get_json()
        user = User.get_by_id(user_id=get_jwt_identity())

        user.seedingDate = update_data["seedingDate"]
        user.postCode = update_data["postCode"]
        user.energyPlan = update_data["energyPlan"]
        


        data = {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'seedingDate' : user.seedingDate,
            'postCode' : user.postCode,
            'energyPlan' : user.energyPlan
        }
        user.save()        
        
        return data, HTTPStatus.OK
        
        