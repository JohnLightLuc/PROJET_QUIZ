import graphene

from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from django.contrib.auth.models import User


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



class TimemodelsNode(DjangoObjectType):
    class Meta:
        model = Timemodels
        filter_fields = ['date_add', 'date_update','statut']
   
      
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class LevelNode(DjangoObjectType):
    class Meta:
        model = Level
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'description':['exact','icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class QuizNode(DjangoObjectType):
    class Meta:
        model = Quiz
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'max_question':['exact'],
            'correction': ['exact',],
            'level': ['exact'],
            'single_tentative': ['exact'],
            'result_tentative': ['exact'],
            'pourcentage_requis': ['exact'],
            'success_text': ['exact', 'icontains', 'istartswith'],
            'fail_text': ['exact', 'icontains', 'istartswith'],


        }
        order_by = OrderingFilter(
            fields=(
                ('date_add','date_add'),
            )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection






class Image_testNode(DjangoObjectType):
    class Meta:
        model = Image_test
        # Allow for some more advanced filtering here
        filter_fields = {
            'date_update':['exact',],
            'date_add':['exact',],
            'statut':['exact',],


          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        # Allow for some more advanced filtering here
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
            'quiz':['exact',],
            'level':['exact',],
            # 'image_question':['exact',],
            'description': ['exact', 'icontains', 'istartswith'],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class ReponseNode(DjangoObjectType):
    class Meta:
        model = Reponse
        filter_fields = {
            'reponse': ['exact', 'icontains', 'istartswith'],
            'score':['exact',],
            'question':['exact',],
            # 'image_question':['exact',],
            'description': ['exact', 'icontains', 'istartswith'],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class ResultatNode(DjangoObjectType):
    class Meta:
        model = Resultat
        filter_fields = {
            'quiz_id':['exact',],
            'user_id':['exact',],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection



# class ArticleType(DjangoObjectType):
#     class Meta:
#         model = Article
# class CommentaitreType(DjangoObjectType):
#     class Meta:
#         model = Commentaire
# # ...code
# # Change the CreateLink mutation
# class ArticleInput(graphene.InputObjectType):
#     titre = graphene.String()
# class CommentaireInput(graphene.InputObjectType):
#     article_id = graphene.Field(ArticleInput)
#     contenu = graphene.String()


# class CreateCommentaire(graphene.Mutation):
#     commentaitre = graphene.Field(CommentaitreType)
 

  



#     class Arguments:
#         commentaire_data = CommentaireInput(required=True)
      

#     @staticmethod
#     def mutate(root, info, commentaire_data , article_id    ):
#         user = info.context.user or None
#         commentaire = Commentaire.objects.create(**commentaire_data,username=user )
#         return CreateCommentaire(commentaitre=commentaitre)
   

class Query(ObjectType):
    Timemodels = relay.Node.Field(TimemodelsNode)
    # all_Timemodels = DjangoFilterConnectionField(TimemodelsNode)
    
    Level = relay.Node.Field(LevelNode)
    # all_Levels = DjangoFilterConnectionField(LevelNode)

    Quiz = relay.Node.Field(QuizNode)
    # all_Quizs = DjangoFilterConnectionField(QuizNode)

    Image_test = relay.Node.Field(Image_testNode)
    # all_Image_tests = DjangoFilterConnectionField(Image_testNode)


    Question = relay.Node.Field(QuestionNode)
    # all_Questions = DjangoFilterConnectionField(QuestionNode)
    
    Reponse = relay.Node.Field(ReponseNode)
    # all_Reponse = DjangoFilterConnectionField(ReponseNode)
    
    Resultat = relay.Node.Field(ResultatNode)
    # all_Resultat = DjangoFilterConnectionField(ResultatNode)

    
# class Mutation(graphene.ObjectType):
        
#     create_CreateCommentaire = CreateCommentaire.Field()
   