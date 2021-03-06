# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class LevelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'nom',
        'description',
        'image',
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
        'description',
        'image',
    )


class QuizAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'titre',
        'description',
        'level',
        'max_question',
        'correction',
        'single_tentative',
        'result_tentative',
        'pourcentage_requis',
        'success_text',
        'fail_text',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'level',
        'correction',
        'single_tentative',
        'result_tentative',
        'id',
        'date_add',
        'date_update',
        'statut',
        'titre',
        'description',
        'level',
        'max_question',
        'correction',
        'single_tentative',
        'result_tentative',
        'pourcentage_requis',
        'success_text',
        'fail_text',
    )


class Image_testAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'statut', 'image')
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'id',
        'date_add',
        'date_update',
        'statut',
        'image',
    )


class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'level',
        'description',
        'point',
        'contenu',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'level',
        'id',
        'date_add',
        'date_update',
        'statut',
        'level',
        'description',
        'point',
        'contenu',
    )
    raw_id_fields = ('quiz', 'image_question')


class PropositionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'propsition1',
        'propsition2',
        'propsition3',
        'propsition5',
        'question',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'question',
        'id',
        'date_add',
        'date_update',
        'statut',
        'propsition1',
        'propsition2',
        'propsition3',
        'propsition5',
        'question',
    )


class ReponseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'description',
        'reponse',
        'score',
        'question',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'question',
        'id',
        'date_add',
        'date_update',
        'statut',
        'description',
        'reponse',
        'score',
        'question',
    )
    raw_id_fields = ('image_reponse',)


class ResultatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'statut',
        'quiz_id',
        'user_id',
        'note',
        'taux',
    )
    list_filter = (
        'date_add',
        'date_update',
        'statut',
        'quiz_id',
        'user_id',
        'id',
        'date_add',
        'date_update',
        'statut',
        'quiz_id',
        'user_id',
        'note',
        'taux',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Level, LevelAdmin)
_register(models.Quiz, QuizAdmin)
_register(models.Image_test, Image_testAdmin)
_register(models.Question, QuestionAdmin)
_register(models.Proposition, PropositionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.Resultat, ResultatAdmin)
