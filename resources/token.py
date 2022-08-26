from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity


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
        access_token = create_access_token(identity=user.user_id, fresh=True) #whatswrong? p122 update to 3.25 solved the problem.
        #return 'kaposzta'
        refresh_token = create_refresh_token(identity=user.user_id) #https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/
        return {'access_token': access_token, 'refresh_token' : refresh_token}, HTTPStatus.OK

class RefreshResource(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()

        token = create_access_token(identity=current_user, fresh=False)

        return {'token': token}, HTTPStatus.OK
    
