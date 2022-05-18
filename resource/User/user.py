from typing_extensions import Required
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Campo "name" requirido', required=True)
parser.add_argument('email', type=str, help='Campo "email" requirido', required=True)

class ListUser(Resource):
    def get(self, id):
        return {'id': id}

class CreateUser(Resource):
    def post(self):
        args = parser.parse_args()
        return {'args': args}

class DeleteUser(Resource):
    def delete(self, id):
        return {'id': id}
        