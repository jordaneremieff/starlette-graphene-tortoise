import graphene

from myapp.models import User
from myapp.schema.types import UserType


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    user = graphene.Field(UserType)

    async def mutate(self, info, name: str):
        user = await User.create(name=name)
        return CreateUserMutation(user=user)


class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()

    user = graphene.Field(UserType)

    async def mutate(self, info, id: int, name: str = None):
        user = await User.get(id=id)

        if name is not None:
            user.name = name

        await user.save()

        return UpdateUserMutation(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
