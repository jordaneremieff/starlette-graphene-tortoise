import sys
import os
import contextlib

from tortoise import Tortoise, run_async

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

DB_URL = config("DB_URL", cast=str)
DB_MODELS = config("DB_MODELS", cast=CommaSeparatedStrings)


async def init():
    msg = "".join(
        [
            f"This command will create a new database: 'myapp.db', ",
            "any existing database will be DESTROYED...\n\nEnter 'yes' to continue.\n",
        ]
    )
    confirm = input(msg)
    if confirm != "yes":
        sys.exit()

    with contextlib.suppress(FileNotFoundError):
        os.remove("guitarlette.db")

    await Tortoise.init(db_url=DB_URL, modules={"models": DB_MODELS})
    await Tortoise.generate_schemas()


run_async(init())
