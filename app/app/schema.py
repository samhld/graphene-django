import graphene
import tracks.schema
import users.schema

# want to have schema defined in this higher level directory (/app/)
# so create schema here and call the schema.py file objects from here (from tracks.schema, in this case)
class Query(tracks.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, tracks.schema.Mutation, graphene.ObjectType):
    pass

# define schema here
schema = graphene.Schema(query=Query, mutation=Mutation)