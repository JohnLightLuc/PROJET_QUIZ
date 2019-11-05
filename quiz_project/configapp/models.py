from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.

class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True)

    class Meta:
        abstract=True


class FirstSectionIndex(Timemodels):
    """Model definition for FirstSection."""

    # TODO: Define fields here
    image = models.ImageField(upload_to='first_section',)
    titre = models.CharField(max_length=50)
    action = models.CharField(max_length=50)


    class Meta:
        """Meta definition for FirstSection."""

        verbose_name = 'FirstSection'
        verbose_name_plural = 'FirstSections'

class SecondSectionIndex(Timemodels):
    """Model definition for SecondSectionIndex."""

    # TODO: Define fields here
    image = models.ImageField(upload_to='first_section',)
    titre = models.CharField(max_length=50)
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