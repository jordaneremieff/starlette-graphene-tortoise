import sys
import os
import contextlib

from tortoise import Tortoise, run_async

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

DB_URL = config("DB_URL", cast=str)
DB_MODELS = config("DB_MODELS", cast=CommaSeparatedStrings)


async def init(noinput=False):

    if not noinput:
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
        os.remove("myapp.db")

    await Tortoise.init(db_url=DB_URL, modules={"models": DB_MODELS})
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    noinput = "--noinput" in sys.argv
    run_async(init(noinput=noinput))
