from fastapi import FastAPI
from routes.index import message

app = FastAPI()


# app.include_router(user)
app.include_router(message)
