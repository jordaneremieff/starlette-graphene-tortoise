from tortoise import Tortoise
from graphql.execution.executors.asyncio import AsyncioExecutor

from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from myapp.schema import schema

config = Config(".env")


DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URL = config("DATABASE_URL", cast=str)
APP_MODELS = config("APP_MODELS", cast=CommaSeparatedStrings)


app = Starlette(debug=DEBUG)
app.add_route("/graphql", GraphQLApp(schema=schema, executor=AsyncioExecutor()))


@app.on_event("startup")
async def on_startup() -> None:
    await Tortoise.init(db_url=DATABASE_URL, modules={"models": APP_MODELS})


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await Tortoise.close_connections()
