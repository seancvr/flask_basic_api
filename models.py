from marshmallow import Schema, fields
import enum


#Create schemas for api argument and response data
"""
POST todo/tasks
"""
# arguments
class CreateUser(Schema):
    username = fields.String()
    password = fields.String()

# response
class User(Schema): 
    id = fields.UUID()
    created = fields.DateTime()
    username = fields.String()
    password = fields.String()


"""
GET /todo/tasks
"""
# sorting classes
class SortByEnum(enum.Enum):
    task = "username"
    created = "created"

class SortDirectionEnum(enum.Enum):
    asc = "asc"
    desc = "desc"

# arguments
class ListUserParameters(Schema):
    order_by = fields.Enum(SortByEnum, load_default=SortByEnum.created)
    order = fields.Enum(SortDirectionEnum, load_default=SortDirectionEnum.asc)

# response
class UsersList(Schema):
    users = fields.List(fields.Nested(User))


"""
Singelton PUT /tasks/<uuid:task_id>
"""
# arguments
class UpdateUser(Schema):
    username = fields.String() 
    password = fields.String()

 
# explicitly export all classes so they can be import with *
__all__ = [
    "CreateUser",
    "UpdateUser",
    "User",
    "SortByEnum",
    "SortDirectionEnum",
    "ListUserParameters",
    "UsersList"
]