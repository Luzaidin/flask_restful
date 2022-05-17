from typing_extensions import Required
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('user_name', type=str, help='Nome do usuário', required=True)

class User(Resource):
    def get(self, id):
        return {'hello': 'world'}
    def post(self, id):
        args = parser.parse_args()
        return {'hello': 'world'}