import os
import contextlib

from tortoise import Tortoise, run_async

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

DB_URL = config("DB_URL", cast=str)
DB_MODELS = config("DB_MODELS", cast=CommaSeparatedStrings)


async def init(noinput=False):
    with contextlib.suppress(FileNotFoundError):
        os.remove("myapp.db")

    await Tortoise.init(db_url=DB_URL, modules={"models": DB_MODELS})
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init())
