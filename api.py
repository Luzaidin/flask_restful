from flask import Flask
from flask_restful import Api
from resource.User.user import ListUser, CreateUser, DeleteUser

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(ListUser, '/list/user/<int:id>')
api.add_resource(DeleteUser, '/delete/user/<int:id>')
api.add_resource(CreateUser, '/create/user')
DeleteUser

if __name__ == '__main__':
    app.run(debug=True)