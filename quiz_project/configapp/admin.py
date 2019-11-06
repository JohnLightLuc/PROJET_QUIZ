# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class FirstSectionIndexAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'image',
        'titre',
        'action',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'image',
        'titre',
        'action',
    )


class SecondSectionIndexAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'image',
        'titre',
        'action',
        'nom_cours',
        'nombre_cours',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'image',
        'titre',
        'action',
        'nom_cours',
        'nombre_cours',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'titre',
        'description',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'titre',
        'description',
    )


class FirstSectionAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'statut', 'titre')
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'titre',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.FirstSectionIndex, FirstSectionIndexAdmin)
_register(models.SecondSectionIndex, SecondSectionIndexAdmin)
_register(models.Newsletter, NewsletterAdmin)
_register(models.FirstSection, FirstSectionAdmin)
