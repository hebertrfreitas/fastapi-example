from typing import Annotated

from fastapi import Depends, FastAPI
from service.main_service import MainService
from middlewares.profilling_middleware import add_profile_middleware

app = FastAPI()

add_profile_middleware(app)

@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/health')
def health():
    return 'OK'


@app.get('/pokemon')
def get_pokemon(main_service: Annotated[MainService, Depends()]):
    return main_service.pokemon_info()
