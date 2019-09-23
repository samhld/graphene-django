# separate user app
# Django alreaddy provides a robust user model
# the user model Django provides has fields built in like `lastLogin`,`isSuperuser`,`isStaff`,`isActive`, etc.
from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email
        )
        # provided user model has the following `set_` methods
        user.set_password(password)
        user.save()

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()