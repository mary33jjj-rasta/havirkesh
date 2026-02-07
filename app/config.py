
from fastapi import FastAPI
 
from .db import create_db_and_tables

from fastapi_pagination import add_pagination

# Imports routers

from .routers import provinces
from .routers import city
from .routers import village

app = FastAPI(
    title="havirkesht",
    description="project maryam jomehzadeh",
    version="0.0.2",
)

add_pagination(app)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(provinces.router)
app.include_router(city.router)
app.include_router(village.router)

