import uuid
from datetime import datetime, timezone

seed_data = [
    {"username": "Alice", "password": "Alice123"},
    {"username": "Bob", "password": "Bob123"}
]

# Create in memory userstore
users = []
for item in seed_data:
    dict={}
    dict["id"] = uuid.uuid4()
    dict["created"] = datetime.now(timezone.utc)
    dict["username"] = item["username"]
    dict["password"] = item["password"]
    users.append(dict)