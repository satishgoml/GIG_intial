from fastapi import FastAPI

from api.models import Base


from api.auth import router as auth_router


 
from api.utils.database.connection_util import engine
from fastapi.middleware.cors import CORSMiddleware


# Initialization

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
    

# End Initialization



# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Routers
app.include_router(auth_router.router, prefix="/gig/auth", tags=["user"])









