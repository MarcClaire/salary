from django.db import models

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
        ('CEP', 'Certificat d\'Edude Primaire'),
        ('BEPC', 'Brevet d\'Etude du Premier Cycle'),
        ('CQP', 'Certificat de Qualification professionnelle'),
        ('BEB', 'Brevet d\'Etude Professionnelle'),
        ('CAP', 'Certificat d\'Aptitude Professionnelle'),
        ('BAC', 'Baccalauriat'),
        ('LIC', 'Licence'),
        ('MAS', 'Master'),
        ('DOC', 'Doctorat'),
    ]

    diplome = models.CharField(max_length=10, choices=DIPLOME_CHOICES, unique=True)

    def __str__(self):
        return self.diplome

#la classe employé
class Employe(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    lieu_naissance = models.CharField(max_length=255)
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    situation_matrimoniale = models.ForeignKey(SituationMatrimoniale, on_delete=models.CASCADE)
    nombre_enfant = models.IntegerField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    dernier_diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    lettre_motivation = models.FileField(upload_to='lettres_motivation/', blank=True, null=True)
    diplome = models.FileField(upload_to='diplomes/', blank=True, null=True)
    numero_cnss = models.CharField(max_length=20, blank=True, null=True)
    numero_matricule = models.CharField(max_length=20, blank=True, null=True)
    date_naissance = models.DateField()

    def __str__(self):
        return self.nom




#le type de contrat existant dans les structure
class TypeContrat(models.Model):
    TYPE_CONTRAT_CHOICES = [
        ('CDD', 'Contrat à Durée Déterminé'),
        ('CDI', 'Contrat à Durée Indéterminé'),
    ]

    type_contrat = models.CharField(max_length=3, choices=TYPE_CONTRAT_CHOICES, unique=True)

    def __str__(self):
        return self.type_contrat




# la structure bénéficiaire
class Structure(models.Model):
    denomination = models.CharField(max_length=255)
    description_structure = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.denomination



#la classe contrat
class Contrat(models.Model):
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True, to_field='id')
    description_poste = models.TextField()
    description_profil = models.TextField()
    lieu_affectation = models.CharField(max_length=255)
    diplome_requis = models.ForeignKey(Diplome, on_delete=models.CASCADE)
    type_contrat = models.ForeignKey(TypeContrat, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.lieu_affectation


    
