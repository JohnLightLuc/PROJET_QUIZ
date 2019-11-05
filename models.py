
from django.db import models
from django.contrib.auth.models import User


class Mois(models.Model):
    nom = models.CharField(max_length=50)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )



class Level(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    mois = models.ForeignKey(Mois, on_delete=models.CASCADE, related_name='level_mois')
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )


class Stage(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='stage_level')
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )


class Quiz(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateTimeField(auto_now=False, auto_now_add=False)
    duree = models.DurationField()
    statut = models.BooleanField(default=False)
    stage = models.ForeignKey(Stage, on_delete = models.CASCADE, related_name = 'quiz_stage')
    user = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user_quiz')
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )

class Question (models.Model):
    description = models.TextField ()
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    image_quiz = models.ManyToManyField(Image, null=True)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE, related_name = 'question_quiz',)


class Reponse (models.Model):
    description = models.TextField ()
    reponse = models.CharField(max_length=200)
    score = models.IntegerField(default = True )
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    image_reponse = models.ManyToManyField(Image, null=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'question_reponse',)


class Resultat (models.Model):
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, related_name = 'quiz_resultat',)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user',)
    
