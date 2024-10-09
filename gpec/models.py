from django.db import models
from django.utils import timezone
from employe.models import Employe

class Evaluation(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    evaluateur = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='evaluations_effectuees')
    date_evaluation = models.DateField()

    # Critères d'évaluation
    performance_poste = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    qualites_relationnelles = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    engagement_motivation = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    autonomie = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    conformite_organisationnelle = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    commentaires_collaborateur = models.TextField(blank=True)
    commentaires_superieur = models.TextField(blank=True)
    formations_suivies = models.TextField(blank=True)
    besoins_formation = models.TextField(blank=True)

    def moyenne_globale(self):
        return (self.performance_poste + self.qualites_relationnelles +
                self.engagement_motivation + self.autonomie +
                self.conformite_organisationnelle) / 5

class Talent(models.Model):
    POTENTIEL_CHOICES = [
        ('Faible', 'Faible'),
        ('Moyen', 'Moyen'),
        ('Élevé', 'Élevé'),
        ('Exceptionnel', 'Exceptionnel'),
    ]

    employe = models.OneToOneField(Employe, on_delete=models.CASCADE)
    competences_cles = models.TextField(default='Ajoutez des compétences')
    realisations = models.TextField(default='Ajoutez des réalisations')
    potentiel = models.CharField(max_length=20, choices=POTENTIEL_CHOICES)
    objectifs = models.TextField(default='Ajoutez des objectifs')
    plan_developpement = models.TextField(default='Ajoutez un plan de developpement')
    date_evaluation = models.DateField()

    def __str__(self):
        return f"Talent de {self.employe.nom} {self.employe.prenoms}"

class Performance(models.Model):
    RATING_CHOICES = [
        (1, 'Insuffisant'),
        (2, 'À améliorer'),
        (3, 'Satisfaisant'),
        (4, 'Très bon'),
        (5, 'Exceptionnel'),
    ]

    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name='performances')
    date_evaluation = models.DateField()
    objectifs_atteints = models.TextField(default='Ajoutez des objectifs')
    rating = models.IntegerField(choices=RATING_CHOICES)
    commentaires = models.TextField(default='Ajoutez des commentaires')

    def __str__(self):
        return f"Performance de {self.talent.employe.nom} {self.talent.employe.prenoms} - {self.date_evaluation}"

# class DossierPersonnel(models.Model):
#     employe = models.OneToOneField(Employe, on_delete=models.CASCADE)
#     cv = models.FileField(upload_to='cv/')
#     diplomes = models.FileField(upload_to='diplomes/')
#     certificats = models.FileField(upload_to='certificats/')


class DocumentPersonnel(models.Model):
    TYPE_CHOICES = [
        ('CV', 'Curriculum Vitae'),
        ('DIPLOME', 'Diplôme'),
        ('CERTIFICAT', 'Certificat de travail'),
        ('FORMATION', 'Attestation de formation'),
        ('AUTRE', 'Autre document'),
    ]

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='documents')
    type_document = models.CharField(max_length=20, choices=TYPE_CHOICES)
    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='documents_personnels/')
    date_ajout = models.DateField(auto_now_add=True)
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_type_document_display()} - {self.employe.nom} {self.employe.prenoms}"

# Suivi
class Poste(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.titre

class EvolutionCarriere(models.Model):
    TYPE_EVOLUTION = [
        ('PROMOTION', 'Promotion'),
        ('MUTATION', 'Mutation'),
        ('RECLASSEMENT', 'Reclassement'),
    ]
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='evolutions_carriere')
    date_changement = models.DateField()
    type_evolution = models.CharField(max_length=20, choices=TYPE_EVOLUTION)
    ancien_poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True, related_name='anciens_postes')
    nouveau_poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True, related_name='nouveaux_postes')
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employe.nom} - {self.type_evolution} - {self.date_changement}"

class MouvementPersonnel(models.Model):
    TYPE_MOUVEMENT = [
        ('DEPART_RETRAITE', 'Départ en retraite'),
        ('LICENCIEMENT', 'Licenciement'),
        ('DEMISSION', 'Démission'),
        ('DECES', 'Décès'),
        ('AUTRE', 'Autre'),
    ]
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='mouvements')
    date_mouvement = models.DateField()
    type_mouvement = models.CharField(max_length=20, choices=TYPE_MOUVEMENT)
    raison = models.TextField()

    def __str__(self):
        return f"{self.employe.nom} - {self.get_type_mouvement_display()} - {self.date_mouvement}"

class SuiviCarriere(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_embauche = models.DateField()
    poste_actuel = models.CharField(max_length=100)
    historique_postes = models.TextField()

# class PlanRecrutement(models.Model):
#     poste = models.CharField(max_length=100)
#     date_prevue = models.DateField()
#     description = models.TextField()

class PlanRecrutement(models.Model):
    STATUT_CHOICES = [
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
        ('ANNULE', 'Annulé'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(default='descriptions non définis')
    date_debut = models.DateField(default=timezone.now)
    date_fin = models.DateField(default=timezone.now)
    nombre_postes = models.IntegerField(default=0)
    competences_requises = models.TextField(default='Ajoutez des compétences requises')
    departement = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_COURS')

    def __str__(self):
        return self.titre

class CandidatPlan(models.Model):
    STATUT_CHOICES = [
        ('RECU', 'Reçu'),
        ('EN_COURS', 'En cours'),
        ('ACCEPTE', 'Accepté'),
        ('REFUSE', 'Refusé'),
    ]

    plan = models.ForeignKey(PlanRecrutement, on_delete=models.CASCADE, related_name='candidats')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cvs/')
    date_candidature = models.DateField(default=timezone.now)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='RECU')
    commentaires = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.plan.titre}"


# class PointagePresence(models.Model):
#     employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
#     date = models.DateField(default=timezone.now)
#     heure_arrivee = models.TimeField()
#     heure_depart = models.TimeField()

class Pointage(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='pointages')
    date = models.DateField(default=timezone.now)
    heure_arrivee = models.TimeField(null=True, blank=True)
    heure_depart = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employe.nom} - {self.date}"

class Absence(models.Model):
    TYPE_ABSENCE = [
        ('CONGE', 'Congé'),
        ('MALADIE', 'Maladie'),
        ('AUTRE', 'Autre'),
    ]
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='absences')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    type_absence = models.CharField(max_length=20, choices=TYPE_ABSENCE)
    justification = models.TextField(blank=True, default="Notifiez une justification")

    def __str__(self):
        return f"{self.employe.nom} - {self.get_type_absence_display()} - {self.date_debut}"


# class FichePoste(models.Model):
#     titre = models.CharField(max_length=100)
#     description = models.TextField()
#     competences_requises = models.TextField()
class FichePoste(models.Model):
    titre = models.CharField(max_length=200, null=True)
    departement = models.CharField(max_length=100, null=True)
    superieur_hierarchique = models.CharField(max_length=200, null=True)
    missions_principales = models.TextField(default='spécifiiez une mission')
    activites_principales = models.TextField(default="Spécifiez l'activitée principale")
    competences_requises = models.TextField(default='Spécifiez des compétences requises')
    formation_requise = models.TextField(default='Spécifiez des formations')
    experience_requise = models.TextField(default='Spécifiez vos expériences')
    date_creation = models.DateField(auto_now_add=True, null=True)
    date_mise_a_jour = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.titre

class EmployePoste(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    fiche_poste = models.ForeignKey(FichePoste, on_delete=models.CASCADE)
    date_attribution = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.employe.nom} - {self.fiche_poste.titre}"


# class ReferentielCompetences(models.Model):
#     competence = models.CharField(max_length=100)
#     description = models.TextField()
#     niveau = models.IntegerField()
class Competence(models.Model):
    nom = models.CharField(max_length=200, null=True)
    description = models.TextField(default='Décrire vos compétences')
    categorie = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom

class NiveauCompetence(models.Model):
    NIVEAUX = [
        (1, 'Débutant'),
        (2, 'Intermédiaire'),
        (3, 'Avancé'),
        (4, 'Expert'),
    ]
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    niveau = models.IntegerField(choices=NIVEAUX,)
    date_evaluation = models.DateField(auto_now=True, null=True)

    class Meta:
        unique_together = ('competence', 'employe')

    def __str__(self):
        return f"{self.employe.nom} - {self.competence.nom} - Niveau {self.get_niveau_display()}"



