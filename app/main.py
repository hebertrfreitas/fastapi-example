from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from service.pokemon_service import PokemonService
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
def get_pokemon(pokemon_service: Annotated[PokemonService, Depends()]):
    return pokemon_service.pokemon_info()
