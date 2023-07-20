from sqlalchemy.orm import Session
from api.models import UserInfo
from api.auth.schema import UserCreate, UserList


async def get_user(db: Session, email: str):
    return db.query(UserInfo).filter(UserInfo.email == email).first()

async def create_user(db: Session, userData: UserCreate):
    db_user = UserInfo(**userData.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
    
    
    



 