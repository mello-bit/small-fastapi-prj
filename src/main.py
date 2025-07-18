from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.route.router import router

from api.db.session import init_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    


app = FastAPI(lifespan=lifespan)
app.include_router(router=router, prefix='/tasks')

