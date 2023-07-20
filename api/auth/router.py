from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session




from api.auth import schema, crud
from api.utils.authentication.hashing_util import get_password_hash, verify_password
from api.utils.authentication.token_util import create_access_token
from api.utils.database.connection_util import get_db



router = APIRouter()


@router.post(
    "/register",)
async def register(user: schema.UserCreate,
                   response: Response,
                   db: Session = Depends(get_db)
                   ):
    # Check if user already exists
    result = await crud.get_user(db, user.email)
    
    if result:
        raise HTTPException(status_code=400, detail="User already exists") 
    
    # Create new user
    user.hashed_password = get_password_hash(user.hashed_password)
    
    await crud.create_user(db, user)
    return {**user.dict()}

@router.post("/login")
async def login(response: Response,form_data: OAuth2PasswordRequestForm = Depends(),
                  db: Session = Depends(get_db)
                ):
    # Check user existed
    result = await crud.get_user(db, form_data.username)
    
    if not result:
        raise HTTPException(status_code=400, detail="User Not Found")
    
    # Verify password
    user = schema.UserCreate(**result.__dict__)
    verified_password = verify_password(form_data.password, user.hashed_password)
    
    if not verified_password:
        raise HTTPException(status_code=400, detail="Incorrect User or Password")
    
    # Create TOKEN
    expires_in_minutes = 30

    # Create a timedelta object representing the token validity duration
    expires_delta = timedelta(minutes=expires_in_minutes)
    
    access_token = await create_access_token(payload={"sub": user.email}, expires_delta= expires_delta)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user_info" : schema.UserList(**result.__dict__)   
    }
    
    


