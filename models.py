from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# 1- Application cours

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
    point = models.PositiveIntegerField()
    pourcentage = models.DecimalField()
    nombre_tentative = models.PositiveIntegerField()
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

# 2- Application message

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )

class Newletter(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )

# 3- Application configuration

class Etablissement(models.Model):
    nom = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images')
    addresse = models.CharField(max_length=200)
    contact = models.CharField( max_length=50)
    email = models.EmailField()
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    youtube = models.URLField(max_length=200)
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )


class Footer_title(models.Model):
    nom = models.CharField(max_length=50)
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )


class Footer_item(models.Model):
    nom = models.CharField(max_length=50)
    title = models.ForeignKey(Footer_title, on_delete = models.CASCADE, related_name = 'foot_tile')
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_update = models.DateTimeField ( auto_now = True )


# 4- Etudiant

class Etudiant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='etudiant')  
    contacts = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='etudiant/', default='useravatar.png')
    date_naissance = models.DateField(null=True)
    lieu_naissance = models.CharField(max_length=50)
    nationnalite = models.CharField(max_length=50)

    
    @receiver(post_save, sender=User)
    def create_user_etudiant(sender, instance, created, **kwargs):
        if created:
            Etudiant.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_etudiant(sender, instance, created, **kwargs):
        
        instance.etudiant.save()



