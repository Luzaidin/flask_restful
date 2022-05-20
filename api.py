from flask import Flask
from flask_restful import Api
from Model.user import ListAllUsers, ListUser, CreateUser, DeleteUser, UpdateUser

app = Flask(__name__)
api = Api(app)

# RoutesListAllUsers
api.add_resource(ListAllUsers, '/listAll/user')
api.add_resource(ListUser, '/list/user/<int:id>')
api.add_resource(DeleteUser, '/delete/user/<int:id>')
api.add_resource(CreateUser, '/create/user')
api.add_resource(UpdateUser, '/update/user')

@app.route('/')
def index():
    return 'Home'

if __name__ == '__main__':
    app.run(port=5000, debug=True)