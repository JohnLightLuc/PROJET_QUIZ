import graphene

from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from django.contrib.auth.models import User
from comptesApp.schema import UserType

from .models import *

# Graphene will automatically map the Article model's fields onto the ArticleNode.
# This is configured in the ArticleNode's Meta class (as you can see below)
class ExtendedConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)




class NanNode(DjangoObjectType):
    class Meta:
        model = Nan
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'adresse':['exact'],
            'numero': ['exact',],
            'email': ['exact'],
        }
        # order_by = OrderingFilter(
        #     fields=(
        #         ('date_add','date_add'),
        #         ('vues','vues'),
        #     )
        # )
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection






class SocialNode(DjangoObjectType):
    class Meta:
        model = Social
        # Allow for some more advanced filtering here
        filter_fields = {
            'facebook':['exact',],
            'twitter':['exact',],
            'instagram':['exact',],
            'youtube':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class GeolocalisationNode(DjangoObjectType):
    class Meta:
        model = Geolocalisation
        # Allow for some more advanced filtering here
        filter_fields = {
            'latitude':['exact',],
            'longitude':['exact',],
            'url':['exact',],

          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

# Mr Toure faites la mutation des modeles newsletter et contact


class Query(ObjectType):
    Nan = relay.Node.Field(NanNode)
    all_Nans = DjangoFilterConnectionField(NanNode)
    
    Social = relay.Node.Field(SocialNode)
    all_Socials = DjangoFilterConnectionField(SocialNode)

    Geolocalisation = relay.Node.Field(GeolocalisationNode)
    all_Geolocalisations = DjangoFilterConnectionField(GeolocalisationNode)

    
# class Mutation(graphene.ObjectType):
        
#     create_CreateCommentaire = CreateCommentaire.Field()
   