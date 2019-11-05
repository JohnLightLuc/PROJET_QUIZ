```python

from django.contrib.auth.models import User
from tinymce import HTMLField
from django.db import models

class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)

    class Meta:
        abstract=True

# App site

class Nan(Timemodels):
    """Model definition for Nan."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    logo = models.FileField(upload_to='image_nan', max_length=100)
    adresse = models.CharField(max_length=250)
    numero = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)

    class Meta:
        """Meta definition for Nan."""

        verbose_name = 'Nan'
        verbose_name_plural = 'Nans'

    def __str__(self):
        """Unicode representation of Nan."""
        return self.nom

class Social(Timemodels):
    """Model definition for Social."""

    # TODO: Define fields here
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    youtube = models.URLField(max_length=200)


    class Meta:
        """Meta definition for Social."""

        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

class Newsletter(Timemodels):
    """Model definition for Newsletter."""

    # TODO: Define fields here
    email = models.EmailField(, max_length=254)

    class Meta:
        """Meta definition for Newsletter."""

        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class Contact(Timemodels):
    """Model definition for Contact."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Geolocalisation(Timemodels):
    """Model definition for Geolocalisation."""

    # TODO: Define fields here
    latitude = models.PositiveIntegerField()
    longitude = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Geolocalisation."""

        verbose_name = 'Geolocalisation'
        verbose_name_plural = 'Geolocalisations'

# Configuration appp


class FirstSectionIndex(Timemodels):
    """Model definition for FirstSection."""

    # TODO: Define fields here
    image = models.ImageField(upload_to='first_section',)
    titre = HTMLField('Content',null=True)
    action = models.CharField(max_length=50)


    class Meta:
        """Meta definition for FirstSection."""

        verbose_name = 'FirstSection'
        verbose_name_plural = 'FirstSections'

class SecondSectionIndex(Timemodels):
    """Model definition for SecondSectionIndex."""

    # TODO: Define fields here
    image = models.ImageField(upload_to='first_section',)
    titre = HTMLField('Content',null=True)
    action = models.CharField(max_length=50)
    nom_cours = models.CharField(max_length=50)
    nombre_cours = models.PositiveIntegerField()


    class Meta:
        """Meta definition for SecondSectionIndex."""

        verbose_name = 'SecondSectionIndex'
        verbose_name_plural = 'SecondSectionIndexs'


class Newsletter(Timemodels):
    """Model definition for Newsletter."""

    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        """Meta definition for Newsletter."""

        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

class FirstSection(Timemodels):
    """Model definition for FirstSection."""

    # TODO: Define fields here
    titre = models.CharField(max_length=250)

    class Meta:
        """Meta definition for FirstSection."""

        verbose_name = 'FirstSection'
        verbose_name_plural = 'FirstSections'


# quiz app

class Level(Timemodels):
    """Model definition for Level."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    description = HTMLField('Content',null=True)
    image = models.ImageField(upload_to='leve_image',)

    class Meta:
        """Meta definition for Level."""

        verbose_name = 'Level'
        verbose_name_plural = 'Levels'




class Quiz(models.Model):
    """Model definition for Quiz."""

    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    description = HTMLField('Content',null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='levels')
    image = models.ImageField(upload_to='quiz_image',)
    max_question = models.PositiveIntegerField()
    correction = models.BooleanField(default=False)
    single_tentative = models.BooleanField(default=True)
    result_tentative = models.BooleanField()
    pourcentage_requis = models.SmallIntegerField()
    date_debut = models.DateTimeField(auto_now=False, auto_now_add=False)
    duree = models.DurationField()
    success_text = HTMLField('Content',null=True)
    fail_text = HTMLField('Content',null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)


    class Meta:
        """Meta definition for Quiz."""

        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizs'

    def __str__(self):
        """Unicode representation of Quiz."""
        return sellf.titre

class Question(models.Model):
    """Model definition for Question."""

    # TODO: Define fields here
    quiz = models.ManyToManyField(Quiz,related_name='quizs')
    description = models.TextField()
    image = models.ImageField(upload_to='question_image',)
    image_quiz = models.ManyToManyField(Image, null=True)
    contenu = HTMLField('Content',null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.description

class Reponse (models.Model):
    description = models.TextField ()
    reponse = models.CharField(max_length=200)
    score = models.IntegerField(default = True )
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    
    image_reponse = models.ManyToManyField(Image, null=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'question_reponse',)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

class Resultat (models.Model):
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )
    quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, related_name = 'quiz_resultat',)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user',)

```