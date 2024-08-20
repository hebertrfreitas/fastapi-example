from fastapi import FastAPI, Depends
from typing import Annotated
from service.main_service import MainService
app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/health')
def health():
    return 'OK'


@app.get('/pokemon')
def get_pokemon(main_service: Annotated[MainService, Depends()]):
    return main_service.pokemon_info()
