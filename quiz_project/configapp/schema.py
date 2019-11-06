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
        # )
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
   
# Create Input Object Types
class FirstSectionIndexInput(graphene.InputObjectType):
    id = graphene.ID()
    image = graphene.String()
    titre = graphene.String()
    action = graphene..String()


class SecondSectionIndexInput(graphene.InputObjectType):
    id = graphene.ID()
    image = graphene.String()
    titre = graphene.String()
    nom_cours = graphene..String()
    nombre_cours = graphene.Int()


class NewsletterInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()
    description = graphene..String()


class FirstSectionInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()

# Create mutations for FirstSectionIndex
class CreateFirstSectionIndex(graphene.Mutation):
    class Arguments:
        input = FirstSectionIndexInput(required=True)

    ok = graphene.Boolean()
    firstSectionIndex = graphene.Field(FirstSectionIndexNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        firstSectionIndex_instance = FirstSectionIndex(image=input.image,titre=input.titre,action=input.action)
        firstSectionIndex_instance.save()
        return CreateFirstSectionIndex(ok=ok, firstSectionIndex=firstSectionIndex_instance)


class UpdateFirstSectionIndex(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = FirstSectionIndexInput(required=True)

    ok = graphene.Boolean()
    firstSectionIndex = graphene.Field(FirstSectionIndexNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        firstSectionIndex_instance = FirstSectionIndex.objects.get(pk=id)
        if firstSectionIndex_instance:
            ok = True
            firstSectionIndex_instance.image = input.image
            firstSectionIndex_instance.titre = input.titre
            firstSectionIndex_instance.action = input.action
            firstSectionIndex_instance.save()
            return UpdateFirstSectionIndex(ok=ok, firstSectionIndex=firstSectionIndex_instance)
        return UpdateFirstSectionIndex(ok=ok, firstSectionIndex=None)


# Create mutations for SecondSectionIndex
class CreateSecondSectionIndex(graphene.Mutation):
    class Arguments:
        input = SecondSectionIndexInput(required=True)

    ok = graphene.Boolean()
    secondSectionIndexInput = graphene.Field(SecondSectionIndexNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        secondSectionIndex_instance = FirstSectionIndex(image=input.image,titre=input.titre,action=input.action, nom_cours=input.nom_cours, nombre_cours=input.nombre_cours)
        secondSectionIndex_instance.save()
        return CreateSecondSectionIndex(ok=ok, secondSectionIndex= secondSectionIndex_instance)


class UpdateSecondSectionIndex(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = SecondSectionIndexInput(required=True)

    ok = graphene.Boolean()
    secondSectionIndex = graphene.Field(SecondSectionIndexNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        secondSectionIndex_instance = SecondSectionIndex.objects.get(pk=id)
        if secondSectionIndex_instance:
            ok = True
            secondSectionIndex_instance.image = input.image
            secondSectionIndex_instance.titre = input.titre
            secondSectionIndex_instance.action = input.action
            secondSectionIndex_instance.nom_cours = input.nom_cours
            secondSectionIndex_instance.nombre_cours = input.nombre_cours
            secondSectionIndex_instance.save()
            return UpdateSecondSectionIndex(ok=ok, secondSectionIndex=secondSectionIndex_instance)
        return UpdateSecondSectionIndex(ok=ok, secondSectionIndex=None)


# Create mutations for Newsletter
class CreateNewsletter(graphene.Mutation):
    class Arguments:
        input = NewsletterInput(required=True)

    ok = graphene.Boolean()
    newsletter = graphene.Field(NewsletterNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        newsletter_instance = Newsletter(titre=input.titre,description=input.description)
        newsletter_instance.save()
        return CreateNewsletter(ok=ok, newsletter= newsletter_instance)


class UpdateNewsletter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = NewsletterInput(required=True)

    ok = graphene.Boolean()
    newsletter = graphene.Field(NewsletterNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        newsletter_instance = Newsletter.objects.get(pk=id)
        if newsletter_instance:
            ok = True
            newsletter_instance.titre = input.titre
            newsletter_instance.description = input.description
            newsletter_instance.save()
            return UpdateNewsletter(ok=ok, newsletter= newsletter_instance)
        return UpdateNewsletter(ok=ok, newsletter=None)

# Create mutations for FirstSection
class CreateFirstSection(graphene.Mutation):
    class Arguments:
        input = FirstSectionInput(required=True)

    ok = graphene.Boolean()
    firstSection = graphene.Field(FirstSectionNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        firstSection_instance = FirstSection(titre=input.titre)
        irstSection_instance.save()
        return CreateFirstSection(ok=ok, firstSection=firstSection_instance)


class UpdateFirstSection(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = FirstSectionInput(required=True)

    ok = graphene.Boolean()
    firstSection = graphene.Field(FirstSectionNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        firstSection_instance = FirstSection.objects.get(pk=id)
        if firstSection_instance:
            ok = True
            firstSection_instance.titre = input.titre
            firstSection_instance.save()
            return UpdateFirstSection(ok=ok, firstSection= firstSection_instance)
        return UpdateFirstSection(ok=ok, firstSection=None)


class Mutation(graphene.ObjectType):
    create_firstSectionIndex = CreateFirstSectionIndex.Field()
    update_firstSectionIndex = UpdateFirstSectionIndex.Field()

    create_secondSectionIndex = CreateSecondSectionIndex.Field()
    update_secondSectionIndex = UpdateSecondSectionIndex.Field()

    create_newsletter = CreateNewsletter.Field()
    update_newsletter = UpdateNewsletter.Field()

    create_firstSection = CreateFirstSection.Field()
    update_firstSection = UpdateFirstSection.Field()




