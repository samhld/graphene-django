import graphene
import tracks.schema
import users.schema
import graphql_jwt

# want to have schema defined in this higher level directory (/app/)
# so create schema here and call the schema.py file objects from here (from tracks.schema, in this case)
class Query(users.schema.Query, tracks.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, tracks.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

# define schema here
schema = graphene.Schema(query=Query, mutation=Mutation)
