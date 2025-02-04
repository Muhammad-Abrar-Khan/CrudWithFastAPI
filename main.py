from fastapi import FastAPI
import models
from database import engine
from routers import posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
