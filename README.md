# Flask API

Following youtube tutorial [here](https://www.youtube.com/watch?app=desktop&v=mt-0F_5KvQw),
augemented to create a simple user management api

## Environment and dependencies

Make venv
python3 -m venv .venv

Activate venv
source .venv/bin/activate

Install poetry
pip install -U pip setuptools
pip install poetry

Setup poetry environment
poetry init

Add dependencies using poetry
poetry add flask flask-smorest

run the flask server
FLASK_APP=app:server flask run --reload

## Configuration

Creates an instance of the Flask Object

```python
server = Flask(__name__)
```

Create a class for the API config, and pass the config to the Flask server
```python
class APIConfig:
    API_TITLE = "TODO API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_UI_URL = "https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"

server.config.from_object(APIConfig)
```

Create an instance of an API object using flask-smorest
```python
api = Api(server)
```

Create blueprints, collections of url paths that belong together
```python
todo = Blueprint("todo", "todo", url_prefix="/todo", description="TODO API")
```

## Define routes

A normal use case with api endpoints is that they will handle multiple http methods (get, post, put, delete), and we need to handle those methods with different function definitions. The approach here is to uses classes to group multiple http methods for the same url endpoint.

To enable the class to represent a route, we create a class that inherits from the Flask **MethodView** class. **MethodView** allows the creation of views that represent urls as classes.
```python
class TodoCollection(MethodView): 
```

We then model http endpoints as methods of that class:
```python
def get(self, parameters):
    # endpoint logic goes here
```

the @todo.arguments, and @todo.response decorator functions allow define the schema of the input and output data from the API endpoints.


Arguments decorator defines the arguments schema for the API input data. Arguments are received as a http payload by default, but can be passed as query parameters if specified using the **location** variable:
```python
@todo.arguments(ListTaskParameters, location="query")
```

Response decorator defines status code and the schema/data structure of the response. The **response** decorator takes as input the status code of the response and the input schema, in this case **ListTasks**.
```python
@todo.response(status_code=200, schema=TasksList)
```

The data structures of the argument and response data are defined in **models.py** as python classes in the using the **marshmallow** package. The classes inherit from the **Schema** class. The data types of each argument/response argument are defined as class attributes using the **fields** method.


