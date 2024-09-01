import random

import httpx
from fastapi import HTTPException
from loguru import logger

OK = 200


class PokemonService:


    def pokemon_info(self, pokemon_id: int | None = None) -> str:
        if not pokemon_id:
            pokemon_id = random.randint(1, 155)

        try:
            response = httpx.get(url=f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}abc')
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as exc:
            logger.exception(f"An error occurred while trying to fetch pokemon: {exc} ")
            status_error_code = exc.response.status_code if exc.response else 500
            raise HTTPException(status_code=status_error_code,
                                detail=f"An error occurred while trying to fetch pokemon: {exc} ") from exc
