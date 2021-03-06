import graphene

import quizapp.schema
import siteapp.schema
import configapp.schema

class Query(quizapp.schema.Query,siteapp.schema.Query, configapp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(siteapp.schema.Mutation, quizapp.schema.Mutation, configapp.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)