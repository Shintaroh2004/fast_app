from pydantic import BaseModel

json_str='{"id":10,"name":"taro"}'

class User(BaseModel):
    id:int
    name:str

user=User.model_validate_json(json_str)

print(user)

print(type(user))