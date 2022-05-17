from flask import Flask
from flask_restful import Api
from resource.User.user import User

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(User, '/user/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)