from ast import arg
from typing_extensions import Required
from flask_restful import Resource, reqparse
from DB.user import UserCollection

userDB = UserCollection()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Campo "name" requirido', required=True)
parser.add_argument('email', type=str, help='Campo "email" requirido', required=True)

parser_update = reqparse.RequestParser()
parser_update.add_argument('id', type=int, help='Campo "id" requirido', required=True)
parser_update.add_argument('name', type=str, help='Campo "name" requirido', required=True)
parser_update.add_argument('email', type=str, help='Campo "email" requirido', required=True)

class ListAllUsers(Resource):
    def get(self):
        data = userDB.readUser()
        results = []
        for item in data:
            jsonResult = {
                'id': item[0],
                'name': item[1],
                'email': item[2]
            }
            results.append(jsonResult)
        return {'results': results}

class ListUser(Resource):
    def get(self, id):
        data = userDB.listUser(id)
        results = []
        for item in data:
            jsonResult = {
                'id': item[0],
                'name': item[1],
                'email': item[2]
            }
            results.append(jsonResult)
        return {'results': results}

class CreateUser(Resource):
    def post(self):
        args = parser.parse_args()
        userDB.createUser(args['name'], args['email'])
        return {'args': args}

class UpdateUser(Resource):
    def post(self):
        args = parser_update.parse_args()
        userDB.updateUser(args['id'], args['name'], args['email'])
        return {'args': args}

class DeleteUser(Resource):
    def delete(self, id):
        userDB.deleteUser(id)
        return {'id': id}