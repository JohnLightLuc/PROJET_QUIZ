# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class NanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'nom',
        'logo',
        'adresse',
        'numero',
        'email',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'nom',
        'logo',
        'adresse',
        'numero',
        'email',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'facebook',
        'twitter',
        'instagram',
        'youtube',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'facebook',
        'twitter',
        'instagram',
        'youtube',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'statut', 'email')
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'email',
    )


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'nom',
        'email',
        'subject',
        'message',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'nom',
        'email',
        'subject',
        'message',
    )


class GeolocalisationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'latitude',
        'longitude',
        'url',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'latitude',
        'longitude',
        'url',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Nan, NanAdmin)
_register(models.Social, SocialAdmin)
_register(models.Newsletter, NewsletterAdmin)
_register(models.Contact, ContactAdmin)
_register(models.Geolocalisation, GeolocalisationAdmin)
