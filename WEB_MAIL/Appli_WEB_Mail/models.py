from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#Migration ou modification de la base de donnée
#python manage.py makemigrations
#python manage.py migrate

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, mot_de_passe=None, **extra_fields):
        if not email:
            raise ValueError("L'email doit être fourni")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(mot_de_passe)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mot_de_passe=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        return self.create_user(email, mot_de_passe, **extra_fields)


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('utilisateur', 'Utilisateur'),
    ]

    id_utilisateur = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    numero_telephone = models.CharField(max_length=20, null=True, blank=True)  # ➕ numéro tel
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='utilisateur')
    photo_de_profil = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_active = models.BooleanField(default=False)  # ➕ inactif par défaut

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Message(models.Model):
    CATEGORIE_CHOICES = [
        ('Principale', 'Principale'),
        ('Notification', 'Notification'),
    ]
    STATUS_CHOICES = [
        ('Brouillons', 'Brouillons'),
        ('Planifié', 'Planifié'),
        ('Archiver', 'Archiver'),
        ('Corbeille', 'Corbeille'),
        ('Suivie', 'Suivie'),
    ]

    id_message = models.CharField(max_length=20, primary_key=True)
    objet = models.CharField(max_length=200)
    text = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default='Principale')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Brouillons')
    date_envoie = models.DateTimeField(auto_now_add=True)
    date_programmee = models.DateTimeField(blank=True, null=True)
    est_lu = models.BooleanField(default=False)
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes')

    def __str__(self):
        return self.objet


class Attachement(models.Model):
    id_attachement = models.CharField(max_length=20, primary_key=True)
    fichier = models.FileField(upload_to='fichiers/')
    lien = models.URLField(blank=True, null=True)
    drive = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachements')


class Confidentiel(models.Model):
    id_confidentiel = models.CharField(max_length=20, primary_key=True)
    est_confidentiel = models.BooleanField(default=False)
    date_expiration = models.DateField(blank=True, null=True)
    heure_expiration = models.TimeField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='confidentiel')


class Destinataire(models.Model):
    TYPE_CHOICES = [
        ('A', 'A'),
        ('CC', 'CC'),
        ('CCI', 'CCI'),
    ]

    email_destinataire = models.EmailField()
    nom_destinataire = models.CharField(max_length=100)
    prenom_destinataire = models.CharField(max_length=100)
    type_destinataire = models.CharField(max_length=3, choices=TYPE_CHOICES, default='A')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='destinataires')

    def __str__(self):
        return f"{self.nom_destinataire} ({self.email_destinataire})"