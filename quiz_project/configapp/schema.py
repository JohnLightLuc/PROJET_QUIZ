import graphene

from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from django.contrib.auth.models import User
#from comptesApp.schema import UserType

from .models import *



# Create a GraphQL type for  models
class FirstSectionIndexType(DjangoObjectType):
    class Meta:
        model = FirstSectionIndex

class SecondSectionIndexType(DjangoObjectType):
    class Meta:
        model = SecondSectionIndex


class NewsletterType(DjangoObjectType):
    class Meta:
        model = Newsletter

class FirstSectionType(DjangoObjectType):
    class Meta:
        model = FirstSection

# Create a Query type
class Query(ObjectType):
    firstSectionIndex = graphene.Field(FirstSectionIndexType, id=graphene.Int())
    firstSectionIndexs = graphene.List(FirstSectionIndexType)

    secondSectionIndex = graphene.Field(SecondSectionIndexType, id=graphene.Int())
    secondSectionIndexs = graphene.List(SecondSectionIndexType)

    newsletter = graphene.Field(NewsletterType, id=graphene.Int())
    newsletters= graphene.List(NewsletterType)

    firstSection = graphene.Field(FirstSectionType, id=graphene.Int())
    firstSections= graphene.List(FirstSectionType)

    def resolve_firstSectionIndex(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return FirstSectionIndex.objects.get(pk=id)

        return None

    def resolve_secondSectionIndex(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return SecondSectionIndex.objects.get(pk=id)

        return None

    def resolve_newsletter(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Newsletter.objects.get(pk=id)

        return None

    def resolve_firstSection(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return FirstSection.objects.get(pk=id)

        return None

    def resolve_firstSectionIndexs(self, info, **kwargs):
        return FirstSectionIndex.objects.all() 

    def resolve_SecondSectionIndexs(self, info, **kwargs):
        return SecondSectionIndex.objects.all()

    def resolve_newsletters(self, info, **kwargs):
        return Newsletter.objects.all()

    def resolve_firstSections(self, info, **kwargs):
        return FirstSection.objects.all()


# class Query(ObjectType):
#     FirstSectionIndex = relay.Node.Field(FirstSectionIndexNode)
#     all_FirstSectionIndexs = DjangoFilterConnectionField(FirstSectionIndexNode)
    
#     SecondSectionIndex = relay.Node.Field(SecondSectionIndexNode)
#     all_SecondSectionIndexs = DjangoFilterConnectionField(SecondSectionIndexNode)

#     Newsletter = relay.Node.Field(NewsletterNode)
#     all_Newsletters = DjangoFilterConnectionField(NewsletterNode)

#     Commentaire = relay.Node.Field(CommentaireNode)
#     all_Commentaires = DjangoFilterConnectionField(CommentaireNode)


#     FirstSection = relay.Node.Field(FirstSectionNode)
#     all_FirstSections = DjangoFilterConnectionField(FirstSectionNode)
    
    
# class Mutation(graphene.ObjectType):
        
#     create_CreateCommentaire = CreateCommentaire.Field()
   
# Create Input Object Types
class FirstSectionIndexInput(graphene.InputObjectType):
    id = graphene.ID()
    image = graphene.String()
    titre = graphene.String()
    action = graphene.String()


class SecondSectionIndexInput(graphene.InputObjectType):
    id = graphene.ID()
    image = graphene.String()
    titre = graphene.String()
    nom_cours = graphene.String()
    nombre_cours = graphene.Int()


class NewsletterInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()
    description = graphene.String()


class FirstSectionInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()

# Create mutations for FirstSectionIndex
class CreateFirstSectionIndex(graphene.Mutation):
    class Arguments:
        input = FirstSectionIndexInput(required=True)

    ok = graphene.Boolean()
    firstSectionIndex = graphene.Field(FirstSectionIndexType)

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
    firstSectionIndex = graphene.Field(FirstSectionIndexType)

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
    secondSectionIndexInput = graphene.Field(SecondSectionIndexType)

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
    secondSectionIndex = graphene.Field(SecondSectionIndexType)

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
    newsletter = graphene.Field(NewsletterType)

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
    newsletter = graphene.Field(NewsletterType)

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
    firstSection = graphene.Field(FirstSectionType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        firstSection_instance = FirstSection(titre=input.titre)
        firstSection_instance.save()
        return CreateFirstSection(ok=ok, firstSection=firstSection_instance)


class UpdateFirstSection(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = FirstSectionInput(required=True)

    ok = graphene.Boolean()
    firstSection = graphene.Field(FirstSectionType)

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




