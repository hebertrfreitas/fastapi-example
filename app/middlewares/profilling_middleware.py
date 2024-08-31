from pyinstrument import Profiler
from pyinstrument.renderers import HTMLRenderer
from fastapi import FastAPI, Request
from pathlib import Path


def add_profile_middleware(app: FastAPI):
    @app.middleware("http")
    async def profile_request(request: Request, call_next):
        """Profile the current request

        Taken from https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-a-web-request-in-fastapi
        with slight improvements.

        """

        current_dir = Path(__file__).parent

        if request.query_params.get("profile", False):
            with Profiler(interval=0.001, async_mode="enabled") as profiler:
                response = await call_next(request)

            with open(current_dir / f"../profile.html", "w") as out:
                out.write(profiler.output(renderer=HTMLRenderer()))
            return response
        return await call_next(request)
