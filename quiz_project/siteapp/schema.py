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

class NewsletterNode(DjangoObjectType):
    class Meta:
        model = Social
        # Allow for some more advanced filtering here
        filter_fields = ['email']
        interfaces = (relay.Node, )

class ContactNode(DjangoObjectType):
    class Meta:
        model = Contact
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'email':['exact',],
            'subject':['exact',],
            'subject':['exact',],

        }
        interfaces = (relay.Node, )


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

# ------------------------------------------------------------------------

# Create Input Object Types
class NanInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    logo = graphene.String()
    adresse = graphene.String()
    numero = graphene.Int()
    email = graphene.String()

class SocialInput(graphene.InputObjectType):
    id = graphene.ID()
    facebook = graphene.String()
    twitter = graphene.String()
    instagram = graphene.String()
    youtube = graphene.String()
   
class NewsletterInput(graphene.InputObjectType):
    id = graphene.ID()
    email = graphene.String()

class ContactInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    email = graphene.String()
    subject = graphene.String()
    message = graphene.String()

class GeolocalisationInput(graphene.InputObjectType):
    id = graphene.ID()
    latitude = graphene.Int()
    longitude = graphene.Int()
    url = graphene.String()


# Create mutations for Nan
class CreateNan(graphene.Mutation):
    class Arguments:
        input = NanInput(required=True)

    ok = graphene.Boolean()
    nan = graphene.Field(NanNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        nan_instance = Nan(nom=input.nom,logo=input.logo, adresse=input.adresse, numero=input.numero, email=input.email )
        nan_instance.save()
        return CreateNan(ok=ok, nan=nan_instance)

class UpdateNan(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = NanInput(required=True)

    ok = graphene.Boolean()
    nan = graphene.Field(NanNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        nan_instance = Nan.objects.get(pk=id)
        if nan_instance:
            ok = True
            nan_instance.nom = input.nom
            nan_instance.logo = input.logo
            nan_instance.adresse = input.adresse
            nan_instance.numero = input.numero
            nan_instance.email = input.email
            nan_instance.save()
            return UpdateNan(ok=ok, nan=nan_instance)
        return UpdateNan(ok=ok, nan=None)


# Create mutations for Social
class CreateSocial(graphene.Mutation):
    class Arguments:
        input = SocialInput(required=True)

    ok = graphene.Boolean()
    social = graphene.Field(SocialNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        social_instance = Social(facebook=input.facebook, twitter=input.twitter, instagram=input.instagram, youtube=input.youtube)
        social_instance.save()
        return CreateSocial(ok=ok, social=social_instance)

class UpdateSocial(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = SocialInput(required=True)

    ok = graphene.Boolean()
    social = graphene.Field(SocialNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        social_instance = Social.objects.get(pk=id)
        if social_instance:
            ok = True
            social_instance.facebook = input.facebook
            social_instance.twitter = input.twitter
            social_instance.instagram = input.instagram
            social_instance.youtube = input.youtube
            social_instance.save()
            return UpdateSocial(ok=ok, social=social_instance)
        return UpdateSocial(ok=ok, social=None)

# Create mutations for Newsletter
class CreateNewsletter(graphene.Mutation):
    class Arguments:
        input = NewsletterInput(required=True)

    ok = graphene.Boolean()
    newsletter = graphene.Field(NewsletterNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        newsletter_instance = Newsletter(email=input.email)
        newsletter_instance.save()
        return CreateNewsletter(ok=ok, newsletter=newsletter_instance)

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
            newsletter_instance.email = input.email
            newsletter_instance.save()
            return UpdateNewsletter(ok=ok, newsletter=newsletter_instance)
        return UpdateNewsletter(ok=ok, newsletter=None)


# Create mutations for Contact
class CreateContact(graphene.Mutation):
    class Arguments:
        input = ContactInput(required=True)

    ok = graphene.Boolean()
    contact = graphene.Field(ContactNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        contact_instance = Contact(nom=input.nom,email=input.email, subject=input.subject, message=input.message )
        contact_instance.save()
        return CreateContact(ok=ok, contact=contact_instance)

class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ContactInput(required=True)

    ok = graphene.Boolean()
    contact = graphene.Field(ContactNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        contact_instance = Contact.objects.get(pk=id)
        if contact_instance:
            ok = True
            contact_instance.nom = input.nom
            contact_instance.email = input.email
            contact_instance.subject = input.subject
            contact_instance.message = input.message
            contact_instance.save()
            return UpdateContact(ok=ok, newsletter=contact_instance)
        return UpdateContact(ok=ok, contact=None)

# Create mutations for actors
class CreateGeolocalisation(graphene.Mutation):
    class Arguments:
        input = GeolocalisationInput(required=True)

    ok = graphene.Boolean()
    geolocalisation = graphene.Field(GeolocalisationNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        geolocalisation_instance = Geolocalisation(latitude=input.latitude, longitude=input.longitude, url=input.url)
        geolocalisation_instance.save()
        return CreateGeolocalisation(ok=ok, geolocalisation=geolocalisation_instance)

class UpdateGeolocalisation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = GeolocalisationInput(required=True)

    ok = graphene.Boolean()
    geolocalisation = graphene.Field(GeolocalisationNode)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        geolocalisation_instance = Geolocalisation.objects.get(pk=id)
        if geolocalisation_instance:
            ok = True
            geolocalisation_instance.latitude = input.latitude
            geolocalisation_instance.longitude = input.longitude
            geolocalisation_instance.url = input.url
            geolocalisation_instance.save()
            return UpdateGeolocalisation(ok=ok, actor=geolocalisation_instance)
        return UpdateGeolocalisation(ok=ok, actor=None)


class Mutation(graphene.ObjectType):
    create_nan = CreateNan.Field()
    update_nan = UpdateNan.Field()

    create_social = CreateSocial.Field()
    update_social = UpdateSocial.Field()

    create_newsletter = CreateNewsletter.Field()
    update_newsletter = UpdateNewsletter.Field()

    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()

    create_geolocalisation = CreateGeolocalisation.Field()
    update_geolocalisation = UpdateGeolocalisation.Field()