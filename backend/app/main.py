from fastapi import FastAPI
from api import cocktail

app = FastAPI()

app.include_router(cocktail.router)



