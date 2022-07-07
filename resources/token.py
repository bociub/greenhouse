from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from utils import check_password
from models.user import User


class TokenResource(Resource):

    def post(self):

        json_data = request.get_json()

        email = json_data.get('email')
        password = json_data.get('password')

        user = User.get_by_email(email=email)

        if not user or not check_password(password, user.password):
            return {'message': 'username or password is incorrect'}, HTTPStatus.UNAUTHORIZED
        #return 'kaposzta'
        access_token = create_access_token(identity=user.id) #whatswrong? p122 update to 3.25 solved the problem.
        #return 'kaposzta'
        return {'access_token': access_token}, HTTPStatus.OK
