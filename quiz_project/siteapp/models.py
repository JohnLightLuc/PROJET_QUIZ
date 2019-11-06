from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True)

    class Meta:
        abstract=True


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
    email = models.EmailField(max_length=254)

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
    url = models.URLField(max_length=200)

    class Meta:
        """Meta definition for Geolocalisation."""

        verbose_name = 'Geolocalisation'
        verbose_name_plural = 'Geolocalisations'