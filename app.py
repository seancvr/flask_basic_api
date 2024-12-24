from flask import Flask, abort
from flask_smorest import Api, Blueprint
from flask.views import MethodView
import uuid
from datetime import datetime, timezone
from data import users
from models import *

# Create an instance of the Flask object
server = Flask(__name__) 

# Create a class for the API config and pass it to the Flask server
class APIConfig:
    API_TITLE = "MANAGE USERS API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

server.config.from_object(APIConfig)

# Create instance of an API object using flask-smorest
api = Api(server)

# create manage blueprint, collections of url paths that belong together
manage = Blueprint("manage", "manage", url_prefix="/manage", description="MANAGE API")

"""
Create routes/views
"""
# Collection endpoints
@manage.route("/users")
class TodoCollection(MethodView): 
    # POST endpoint
    @manage.arguments(CreateUser) 
    @manage.response(status_code=201, schema=User) # 201 for resource creation
    def post(self, user):
        user["id"] = uuid.uuid4()
        user["created"] = datetime.now(timezone.utc)
        users.append(user)
        return users

    # GET endpoint
    @manage.arguments(ListUserParameters, location="query")
    @manage.response(status_code=200, schema=UsersList)
    def get(self, parameters):
        return {
            "users": sorted(
                users,
                key=lambda user: user[parameters["order_by"].value],
                reverse=parameters["order"] == SortDirectionEnum.desc,
            )
        }
    
# Singleton endpoints    
@manage.route("/users/<uuid:user_id>")
class TodoTask(MethodView):

    # get endpoint
    @manage.response(status_code=200, schema=User)
    def get(self, user_id): 
        for user in users:
            if user["id"] == user_id:
                return user
        abort(404, f"Task with ID {user_id} not found.")

    # PUT endpoint
    @manage.arguments(UpdateUser)
    @manage.response(status_code=200, schema=User)    
    def put(self, payload, user_id): 
        for user in user:
            if user["id"] == user_id:
                user["username"] == payload["username"]
                user["password"] = payload["password"]
                return user
        abort(404, f"Task with ID {user_id} not found.")

    # DELETE endpoint
    @manage.response(status_code=204) # 204 for resource deletetion
    def delete(self, user_id):
        for index, user in enumerate(users):
            if user["id"] == user_id:
                users.pop(index)
                return
        abort(404, f"Task with ID {user_id} not found")


# register Blueprint with application object, keep at the bottom of the file
api.register_blueprint(manage)
