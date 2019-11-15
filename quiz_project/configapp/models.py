from django.db import models
from django.contrib.auth.models import User

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
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default="description")
    action = models.CharField(max_length=50)
    nom_cours1 = models.CharField(max_length=50)
    nombre_cours1 = models.PositiveIntegerField()
    nom_cours2 = models.CharField(max_length=50, default='Nom')
    nombre_cour2 = models.PositiveIntegerField(default=0)
    nom_cours3 = models.CharField(max_length=50, default='Nom')
    nombre_cours3 = models.PositiveIntegerField(default=0)


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