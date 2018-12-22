import graphene


class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
