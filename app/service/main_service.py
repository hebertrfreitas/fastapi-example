import random

import httpx


class MainService:

    def pokemon_info(self, pokemon_id: int | None = None) -> str:
        if not pokemon_id:
            pokemon_id = random.randint(1, 155)

        try:
            response = httpx.get(
                url=f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
            )
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f'Exception: {e}')
            raise e
