from pydantic import BaseModel, Field

class UserList(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    
class UserCreate(UserList):
    hashed_password: str
    
    