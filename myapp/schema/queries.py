import graphene

from myapp.models import User
from myapp.schema.types import UserType
from myapp.schema.mutations import Mutation


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    async def resolve_all_users(self, info):
        users = await User.all()
        return users

    async def resolve_user(self, info, id):
        user = await User.get(id=id)
        return user
