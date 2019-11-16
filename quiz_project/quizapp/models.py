from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True)

    class Meta:
        abstract=True


class Level(Timemodels):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="image", default="default.jpg")
    
    def __str__(self):
        """Unicode representation of Level."""
        return self.nom


class Quiz(Timemodels):
    """Model definition for Quiz."""

    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    description = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='quiz_levels')
    max_question = models.PositiveIntegerField()
    correction = models.BooleanField(default=False)
    single_tentative = models.BooleanField(default=True)
    result_tentative = models.BooleanField()
    pourcentage_requis = models.SmallIntegerField()
    success_text = models.TextField()
    fail_text = models.TextField()
    


    class Meta:
        """Meta definition for Quiz."""

        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizs'

    def __str__(self):
        """Unicode representation of Quiz."""
        return self.titre

class Image_test(Timemodels):
    image = models.ImageField(upload_to='images')

    class Meta:
        """Meta definition for Image_test."""

        verbose_name = 'Image_test'
        verbose_name_plural = 'Image_tests'


class Question(Timemodels):
    """Model definition for Question."""

    # TODO: Define fields here
    quiz = models.ManyToManyField(Quiz,related_name='quizs')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='levels')
    description = models.TextField()
    point = models.SmallIntegerField(default = 0)
    contenu = HTMLField('content')
    image_question = models.ManyToManyField(Image_test)
    

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.description

class Proposition(Timemodels):
    propsition1 = models.CharField(max_length=200)
    propsition2 = models.CharField(max_length=200)
    propsition3 = models.CharField(max_length=200)
    propsition5 = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'proposition_question')

    class Meta:
        """Meta definition for Proposition."""

        verbose_name = 'Proposition'
        verbose_name_plural = 'Propositions'




class Reponse (Timemodels):
    description = models.TextField ()
    reponse = models.CharField(max_length=200)
    score = models.IntegerField(default = True )
    image_reponse = models.ManyToManyField(Image_test)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'question_reponse',)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Reponse'
        verbose_name_plural = 'Reponses'

class Resultat (Timemodels):
    quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, related_name = 'quiz_resultat',)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user',)
    note = models.SmallIntegerField(default = 0)
    taux = models.SmallIntegerField(default = 0)

    # @property
    # def pourcentage(self):
    #    #total = Resultat.objects.all().aggregate(ma_sum = Sum('nombre_hbitants'))
    #    participants = Resultat.objects.all().count()

    #    return round(pourcent, 2)
        