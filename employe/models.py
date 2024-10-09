from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from datetime import timedelta
from django.utils import timezone
#from elementSal.models import Elementsalaire
# Create your models here.

#les differents types de situation matrimonialeque peux avoir un employé
class SituationMatrimoniale(models.Model):
    SITUATION_MATRIMONIALE_CHOICES = [
        ('Marié', 'Marié'),
        ('Célibataire', 'Célibataire'),
        ('Veuve', 'Veuve'),
        ('Veuf', 'Veuf'),
        ('Divorcé', 'Divorcé'),
    ]

    situation_matrimoniale = models.CharField(max_length=50, choices=SITUATION_MATRIMONIALE_CHOICES, unique=True)

    def __str__(self):
        return self.situation_matrimoniale


#les differents types de categorie d'employé
class Categorie(models.Model):
    CATEGORIE_CHOICES = [
        ('Technicien', 'Technicien'),
        ('Ingénieur', 'Ingénieur'),
    ]

    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES, unique=True)

    def __str__(self):
        return self.categorie


#les differents types de spécialité
class Specialite(models.Model):
    SPECIALITE_CHOICES = [
        ('Mathématique', 'Mathématique'),
        ('Chimie', 'Chimie'),
        ('Droit', 'Droit'),
        ('Resource Humaine', 'Resource Humaine'),
        ('Gestion Commerciale', 'Gestion Commerciale'),
    ]

    specialite = models.CharField(max_length=50, choices=SPECIALITE_CHOICES, unique=True)

    def __str__(self):
        return self.specialite



#les differents types de diplôme
class Diplome(models.Model):
    DIPLOME_CHOICES = [
        ('Certificat d\'Edude Primaire', 'Certificat d\'Edude Primaire'),
        ('Brevet d\'Etude du Premier Cycle', 'Brevet d\'Etude du Premier Cycle'),
        ('Certificat de Qualification professionnelle', 'Certificat de Qualification professionnelle'),
        ('Brevet d\'Etude Professionnelle', 'Brevet d\'Etude Professionnelle'),
        ('Certificat d\'Aptitude Professionnelle', 'Certificat d\'Aptitude Professionnelle'),
        ('Baccalauriat', 'Baccalauriat'),
        ('Licence', 'Licence'),
        ('Master', 'Master'),
        ('Doctorat', 'Doctorat'),
    ]

    diplome = models.CharField(max_length=50, choices=DIPLOME_CHOICES, unique=True)

    def __str__(self):
        return self.diplome

class SecteurActivite(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

#///////////
class Employe(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    lieu_naissance = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    numero_cnib = models.CharField(max_length=10, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    situation_matrimoniale = models.ForeignKey(SituationMatrimoniale, on_delete=models.CASCADE, null=True, blank=True)
    nombre_enfant = models.IntegerField(default=0)
    telephone = PhoneNumberField()
    email = models.EmailField(null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    dernier_diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE, null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, blank=True)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE, null=True, blank=True)
    option = models.CharField(max_length=255, null=True, blank=True)
    secteur_activite = models.ForeignKey(SecteurActivite, on_delete=models.SET_NULL, null=True)
    numero_cnss = models.CharField(max_length=20, null=True, blank=True)
    numero_matricule = models.CharField(max_length=20, null=True, blank=True)
    nom_pere = models.CharField(max_length=255, null=True, blank=True)
    nom_mere = models.CharField(max_length=255, null=True, blank=True)
    personne_prevenir = models.CharField(max_length=255, null=True, blank=True)
    telephone_prevenir = PhoneNumberField(null=True, blank=True)
    photo_cnib = models.ImageField(upload_to='photos_cnib/', null=True, blank=True)
    photo_identite = models.ImageField(upload_to='photos_identite/', null=True, blank=True)
    sous_couvert = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenoms} {self.numero_matricule}"

class Dossiers(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    libelle=models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.libelle



#le type de contrat existant dans les structure
class TypeContrat(models.Model):
    libelle=models.CharField(max_length=50,null=True)
    file = models.FileField(upload_to='contrats/', blank=True, null=True)
    def __str__(self):
        return self.libelle


class ModeCalcule(models.Model):
    MODE_Calcul_CHOICES = [
        ('PARTICULIER', 'PARTICULIER'),
        ('CLASSIQUE', 'CLASSIQUE'),
    ]

    mode_calcul = models.CharField(max_length=50, choices=MODE_Calcul_CHOICES, unique=True)

    def __str__(self):
        return self.mode_calcul



# la structure bénéficiaire
class Structure(models.Model):
    denomination = models.CharField(max_length=255)
    description_structure = models.TextField(null=True)
    telephone = PhoneNumberField(null=True)
    email = models.EmailField(null=True)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.denomination


from datetime import timedelta
from django.utils import timezone

class Contrat(models.Model):
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, blank=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True, blank=True)
    poste = models.CharField(max_length=255, null=True)
    description_poste = models.TextField(null=True, blank=True)
    description_profil = models.TextField(null=True, blank=True)
    lieu_affectation = models.CharField(max_length=255)
    diplome_requis = models.ForeignKey(Diplome, on_delete=models.CASCADE, null=True, blank=True)
    type_contrat = models.ForeignKey(TypeContrat, on_delete=models.CASCADE, null=True, blank=True)
    cadre = models.BooleanField(default=False)
    mode_calcul = models.ForeignKey(ModeCalcule, on_delete=models.CASCADE)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)

    # Nouveaux champs pour la gestion de la retraite
    age_legal_retraite = models.IntegerField(default=62)
    date_retraite_prevue = models.DateField(null=True, blank=True)

    # Informations salariales
    salaire_base = models.FloatField(default=0)
    indemnite_logement = models.FloatField(default=0, null=True)
    indemnite_transport = models.FloatField(default=0, null=True)
    indemnite_fonction = models.FloatField(default=0, null=True)
    indemnite_risque = models.FloatField(default=0, null=True)
    prime_nourriture = models.FloatField(default=0, null=True)
    prime_lait = models.FloatField(default=0, null=True)
    prime_salissure = models.FloatField(default=0, null=True)
    prime_astreinte = models.FloatField(default=0, null=True)
    nombre_annee_travail = models.IntegerField(default=0, null=True)
    prime_anciennete = models.BooleanField(default=False, null=True)
    prime_quart = models.BooleanField(default=False)
    prime_panier = models.BooleanField(default=False)
    augmentation_octobre_2019 = models.FloatField(default=False)
    augementation_special_pourcentage = models.FloatField(default=False)
    sursalaire = models.FloatField(default=False)

    # Types de personnel et nature de revenu
    TYPE_PERSONNEL_CHOICES = [
        ('PER', 'Permanent'),
        ('JOU', 'Journalier'),
        ('STA', 'Stagiaire'),
    ]
    type_personnel = models.CharField(
        max_length=3,
        choices=TYPE_PERSONNEL_CHOICES,
        default='PER',
        verbose_name="Type de personnel"
    )

    NATURE_REVENU_CHOICES = [
        ('S', 'Salaire'),
        ('R', 'Rappel'),
        ('A', 'Autres'),
    ]
    nature_revenu = models.CharField(
        max_length=1,
        choices=NATURE_REVENU_CHOICES,
        default='S',
        verbose_name="Nature du revenu"
    )

    def save(self, *args, **kwargs):
        """
        Méthode save() pour calculer automatiquement la date de retraite prévue
        si elle n'est pas encore définie.
        """
        if not self.date_retraite_prevue and self.employe and self.employe.date_naissance:
            self.date_retraite_prevue = self.employe.date_naissance.replace(
                year=self.employe.date_naissance.year + self.age_legal_retraite
            )
        super(Contrat, self).save(*args, **kwargs)

    def calculer_date_retraite(self):
        """
        Méthode qui calcule et retourne la date de retraite prévue si elle
        n'est pas encore calculée.
        """
        if not self.date_retraite_prevue and self.employe and self.employe.date_naissance:
            self.date_retraite_prevue = self.employe.date_naissance.replace(
                year=self.employe.date_naissance.year + self.age_legal_retraite
            )
            self.save()
        return self.date_retraite_prevue

    def annees_avant_retraite(self):
        """
        Méthode pour calculer le nombre d'années restantes avant la retraite
        en fonction de la date de retraite prévue.
        """
        if self.date_retraite_prevue:
            aujourd_hui = timezone.now().date()
            return (self.date_retraite_prevue - aujourd_hui).days // 365
        return None

#la classe contrat
# class Contrat(models.Model):
#     structure = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, blank=True)
#     employe = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True, blank=True)
#     poste=models.CharField(max_length=255, null=True)
#     description_poste = models.TextField(null=True, blank=True)
#     description_profil = models.TextField(null=True, blank=True)
#     lieu_affectation = models.CharField(max_length=255)
#     diplome_requis = models.ForeignKey(Diplome, on_delete=models.CASCADE, null=True, blank=True)
#     type_contrat = models.ForeignKey(TypeContrat, on_delete=models.CASCADE, null=True, blank=True)
#     cadre = models.BooleanField(default=False)
#     #element_salaire=models.ForeignKey(Elementsalaire, on_delete=models.CASCADE)
#     mode_calcul = models.ForeignKey(ModeCalcule, on_delete=models.CASCADE)
#     date_debut = models.DateField(null=True, blank=True)
#     date_fin = models.DateField(null=True, blank=True) 
#     #duree = models.IntegerField(null=True, blank=True, help_text="Durée en mois pour CDD")

#     # Nouveaux champs pour la gestion de la retraite
#     age_legal_retraite = models.IntegerField(default=62)
#     date_retraite_prevue = models.DateField(null=True, blank=True)


#     salaire_base = models.FloatField(default=0)
#     indemnite_logement = models.FloatField(default=0, null=True)
#     indemnite_transport = models.FloatField(default=0, null=True)
#     indemnite_fonction = models.FloatField(default=0, null=True)
#     indemnite_risque = models.FloatField(default=0, null=True)
#     prime_nourriture = models.FloatField(default=0, null=True)
#     prime_lait = models.FloatField(default=0, null=True)
#     prime_salissure = models.FloatField(default=0, null=True)
#     prime_astreinte = models.FloatField(default=0, null=True)
#     nombre_annee_travail = models.IntegerField(default=0, null=True)
#     prime_anciennete = models.BooleanField(default=False, null=True)
#     prime_quart = models.BooleanField(default=False)
#     prime_panier = models.BooleanField(default=False)
#     augmentation_octobre_2019 = models.FloatField(default=False)
#     augementation_special_pourcentage = models.FloatField(default=False)
#     sursalaire = models.FloatField(default=False)
#     #Nouvelle fonctionnalité
#     TYPE_PERSONNEL_CHOICES = [
#         ('PER', 'Permanent'),
#         ('JOU', 'Journalier'),
#         ('STA', 'Stagiaire'),
#     ]
#     type_personnel = models.CharField(
#         max_length=3,
#         choices=TYPE_PERSONNEL_CHOICES,
#         default='PER',
#         verbose_name="Type de personnel"
#     )

#     NATURE_REVENU_CHOICES = [
#         ('S', 'Salaire'),
#         ('R', 'Rappel'),
#         ('A', 'Autres'),
#     ]
#     nature_revenu = models.CharField(
#         max_length=1,
#         choices=NATURE_REVENU_CHOICES,
#         default='S',
#         verbose_name="Nature du revenu"
#     )

#     def calculer_date_retraite(self):
#         if not self.date_retraite_prevue:
#             self.date_retraite_prevue = self.employe.date_naissance.replace(year=Employe.date_naissance.year + self.age_legal_retraite)
#             self.save()
#         return self.date_retraite_prevue
    
#     def annees_avant_retraite(self):
#         if self.date_retraite_prevue:
#             aujourd_hui = timezone.now().date()
#             return (self.date_retraite_prevue - aujourd_hui).days // 365
#         return None


    class Media:
        js = ('static/js/contrat.form.js')

class Mois(models.Model):
    libelle=models.CharField(max_length=20, null=True)

class Annee(models.Model):
    exercice=models.CharField(max_length=10, null=True)

class Type_paiement(models.Model):
    code=models.CharField(max_length=10, null=True)
    libelle=models.CharField(max_length=100, null=True)

class Paiement(models.Model):
    salaire_net=models.FloatField(null=True)
    salaire_brut=models.FloatField(null=True)
    salaire_base=models.FloatField(null=True)
    prime_panier=models.FloatField(null=True)
    prime_quart=models.FloatField(null=True)
    prime_ancien=models.FloatField(null=True)
    prime_lait=models.FloatField(null=True)
    prime_nourriture=models.FloatField(null=True)
    indemnite_logement=models.FloatField(null=True)
    indemnite_transport=models.FloatField(null=True)
    indemnite_fonction=models.FloatField(null=True)
    indemnite_risque=models.FloatField(null=True)
    augmentation_octobre_2019 = models.FloatField(null=False, default=0)
    augementation_special_pourcentage = models.FloatField(null=False, default=0)
    sursalaire = models.FloatField(null=False, default=0)
    cotitsation_cnss=models.FloatField(null=True)
    cnss_patronal=models.FloatField(null=True)
    effort_paix=models.FloatField(null=True)
    tpa=models.FloatField(null=True)
    iuts=models.FloatField(null=True)
    surplus_salaire=models.FloatField(null=True)
    relicat_salaire=models.FloatField(null=True)
    type_paiement = models.ForeignKey(Type_paiement, null=True, on_delete=models.CASCADE)
    mois = models.ForeignKey(Mois, null=True, on_delete=models.CASCADE)
    annee = models.ForeignKey(Annee, null=True, on_delete=models.CASCADE)
    payer=models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    contrat=models.ForeignKey(Contrat, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_at)

class Pointage(models.Model):
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, null=True)
    nb_jour_travail_normal=models.IntegerField(null=True)
    nb_h_normal=models.IntegerField(null=True)
    nb_h_15=models.IntegerField(null=True)
    nb_h_35=models.IntegerField(null=True)
    nb_h_50=models.IntegerField(null=True)
    nb_h_60=models.IntegerField(null=True)
    nb_h_120=models.IntegerField(null=True)
    nb_quart=models.IntegerField(null=True)
    nb_jour=models.IntegerField(null=True)
