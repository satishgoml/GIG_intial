from fastapi import FastAPI

from api.models import Base
from api.utils.database.connection_util import engine


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="FastAPI [Python]",
    description="FastAPI Framework",
    version="1.0",
    openapi_url="/openapi.json"
)

Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    pass
    
@app.on_event("shutdown")
async def shutdown():
    pass
    

@app.get("/")
def helloworld():
    return {"Hello": "World"}





