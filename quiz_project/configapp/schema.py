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




class FirstSectionIndexNode(DjangoObjectType):
    class Meta:
        model = FirstSectionIndex
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'action':['exact','icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class SecondSectionIndexNode(DjangoObjectType):
    class Meta:
        model = SecondSectionIndex
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'action': ['exact', 'icontains', 'istartswith'],
            'nom_cours':['exact'],
            'nombre_cours': ['exact',],
        }
        # order_by = OrderingFilter(
        #     fields=(
        #         ('date_add','date_add'),
        #         ('vues','vues'),
        #     )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection






class NewsletterNode(DjangoObjectType):
    class Meta:
        model = Newsletter
        # Allow for some more advanced filtering here
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
            'titre':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class FirstSectionNode(DjangoObjectType):
    class Meta:
        model = FirstSection
        # Allow for some more advanced filtering here
        filter_fields = {
            'titre':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection



class Query(ObjectType):
    FirstSectionIndex = relay.Node.Field(FirstSectionIndexNode)
    all_FirstSectionIndexs = DjangoFilterConnectionField(FirstSectionIndexNode)
    
    SecondSectionIndex = relay.Node.Field(SecondSectionIndexNode)
    all_SecondSectionIndexs = DjangoFilterConnectionField(SecondSectionIndexNode)

    Newsletter = relay.Node.Field(NewsletterNode)
    all_Newsletters = DjangoFilterConnectionField(NewsletterNode)

    Commentaire = relay.Node.Field(CommentaireNode)
    all_Commentaires = DjangoFilterConnectionField(CommentaireNode)


    FirstSection = relay.Node.Field(FirstSectionNode)
    all_FirstSections = DjangoFilterConnectionField(FirstSectionNode)
    
    
# class Mutation(graphene.ObjectType):
        
#     create_CreateCommentaire = CreateCommentaire.Field()
   