from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils import timezone

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['employe', 'evaluateur', 'date_evaluation', 'performance_poste',
                  'qualites_relationnelles', 'engagement_motivation', 'autonomie',
                  'conformite_organisationnelle', 'commentaires_collaborateur',
                  'commentaires_superieur', 'formations_suivies', 'besoins_formation']
        widgets = {
            'date_evaluation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'commentaires_collaborateur': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'commentaires_superieur': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'formations_suivies': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'besoins_formation': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EvaluationForm, self).__init__(*args, **kwargs)
        # Ajouter la classe Bootstrap 'form-control' pour tous les champs restants
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class') is None:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] += ' form-control'

class TalentForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = ['employe', 'competences_cles', 'realisations', 'potentiel', 'objectifs', 'plan_developpement', 'date_evaluation']
        widgets = {
            'date_evaluation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TalentForm, self).__init__(*args, **kwargs)
        # Appliquer la classe Bootstrap à tous les champs
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class') is None:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] += ' form-control'


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['talent', 'date_evaluation', 'objectifs_atteints', 'rating', 'commentaires']
        widgets = {
            'date_evaluation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PerformanceForm, self).__init__(*args, **kwargs)
        # Appliquer la classe Bootstrap à tous les champs
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class') is None:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] += ' form-control'

class DocumentPersonnelForm(forms.ModelForm):
    class Meta:
        model = DocumentPersonnel
        fields = ['employe', 'type_document', 'titre', 'fichier', 'commentaire']

    def __init__(self, *args, **kwargs):
        super(DocumentPersonnelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EvolutionCarriereForm(forms.ModelForm):
    class Meta:
        model = EvolutionCarriere
        fields = ['employe', 'date_changement', 'type_evolution', 'ancien_poste', 'nouveau_poste', 'commentaire']
        widgets = {
            'date_changement': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EvolutionCarriereForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in self.Meta.widgets:
                field.widget.attrs['class'] = 'form-control'


class MouvementPersonnelForm(forms.ModelForm):
    class Meta:
        model = MouvementPersonnel
        fields = ['employe', 'date_mouvement', 'type_mouvement', 'raison']
        widgets = {
            'date_mouvement': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MouvementPersonnelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in self.Meta.widgets:
                field.widget.attrs['class'] = 'form-control'


class PlanRecrutementForm(forms.ModelForm):
    class Meta:
        model = PlanRecrutement
        fields = ['titre', 'description', 'date_debut', 'date_fin', 'nombre_postes', 'competences_requises', 'departement', 'statut']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PlanRecrutementForm, self).__init__(*args, **kwargs)
        # Ajouter la classe Bootstrap 'form-control' à tous les champs
        for field_name, field in self.fields.items():
            if field_name not in self.Meta.widgets:  # Widgets déjà gérés pour les dates
                field.widget.attrs['class'] = 'form-control'


class CandidatPlanForm(forms.ModelForm):
    class Meta:
        model = CandidatPlan
        fields = ['plan', 'nom', 'prenom', 'email', 'telephone', 'cv', 'statut', 'commentaires']

    def __init__(self, *args, **kwargs):
        super(CandidatPlanForm, self).__init__(*args, **kwargs)
        # Ajouter la classe Bootstrap 'form-control' à tous les champs
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class PointageForm(forms.ModelForm):
    class Meta:
        model = Pointage
        fields = ['employe', 'date', 'heure_arrivee', 'heure_depart']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_arrivee': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'heure_depart': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        heure_arrivee = cleaned_data.get('heure_arrivee')
        heure_depart = cleaned_data.get('heure_depart')

        # Vérifier que la date n'est pas dans le futur
        if date and date > timezone.now().date():
            raise ValidationError("La date ne peut pas être dans le futur.")

        # Vérifier que l'heure de départ est après l'heure d'arrivée
        if heure_arrivee and heure_depart and heure_arrivee > heure_depart:
            raise ValidationError("L'heure de départ ne peut pas être antérieure à l'heure d'arrivée.")
        return cleaned_data

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['employe', 'date_debut', 'date_fin', 'type_absence', 'justification']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')
        type_absence = cleaned_data.get('type_absence')

        # Vérifier que la date de début n'est pas après la date de fin
        if date_debut and date_fin and date_debut > date_fin:
            raise ValidationError("La date de début ne peut pas être après la date de fin.")

        # Vérifier que la date de début n'est pas dans le futur
        if date_debut and date_debut > timezone.now().date():
            raise ValidationError("La date de début ne peut pas être dans le futur.")

        return cleaned_data

class FichePosteForm(forms.ModelForm):
    class Meta:
        model = FichePoste
        fields = ['titre', 'departement', 'superieur_hierarchique', 'missions_principales',
                  'activites_principales', 'competences_requises', 'formation_requise',
                  'experience_requise']
        widgets = {
            'missions_principales': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'activites_principales': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'competences_requises': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'formation_requise': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'experience_requise': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FichePosteForm, self).__init__(*args, **kwargs)
        # Ajouter la classe Bootstrap 'form-control' pour tous les champs restants
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class') is None:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] += ' form-control'
                

    def clean(self):
        cleaned_data = super().clean()
        titre = cleaned_data.get('titre')
        superieur_hierarchique = cleaned_data.get('superieur_hierarchique')
        missions_principales = cleaned_data.get('missions_principales')

        # Valider que le titre n'est pas vide
        if not titre:
            raise ValidationError("Le titre ne peut pas être vide.")

        # Empêcher l'auto-attribution du supérieur hiérarchique
        if superieur_hierarchique and superieur_hierarchique == cleaned_data.get('employe'):
            raise ValidationError("L'employé ne peut pas être son propre supérieur hiérarchique.")

        # Valider la longueur minimale des missions principales
        if missions_principales and len(missions_principales) < 10:
            raise ValidationError("Les missions principales doivent contenir au moins 10 caractères.")

        return cleaned_data

class EmployePosteForm(forms.ModelForm):
    class Meta:
        model = EmployePoste
        fields = ['employe', 'fiche_poste']
        widgets = {
            'employe': forms.Select(attrs={'class': 'form-control'}),
            'fiche_poste': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        employe = cleaned_data.get('employe')
        fiche_poste = cleaned_data.get('fiche_poste')

        # Valider qu'un employé n'est pas déjà assigné à cette fiche de poste
        if EmployePoste.objects.filter(employe=employe, fiche_poste=fiche_poste).exists():
            raise ValidationError("Cet employé est déjà assigné à cette fiche de poste.")

        return cleaned_data

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['nom', 'description', 'categorie']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nom = cleaned_data.get('nom')
        description = cleaned_data.get('description')

        # Vérifier que le nom de la compétence n'est pas vide ou trop court
        if not nom or len(nom) < 3:
            raise ValidationError("Le nom de la compétence doit contenir au moins 3 caractères.")

        # Vérifier que la description n'est pas vide
        if not description or len(description) < 10:
            raise ValidationError("La description doit contenir au moins 10 caractères.")

        return cleaned_data

class NiveauCompetenceForm(forms.ModelForm):
    class Meta:
        model = NiveauCompetence
        fields = ['competence', 'employe', 'niveau']
        widgets = {
            'competence': forms.Select(attrs={'class': 'form-control'}),
            'employe': forms.Select(attrs={'class': 'form-control'}),
            'niveau': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        competence = cleaned_data.get('competence')
        employe = cleaned_data.get('employe')
        niveau = cleaned_data.get('niveau')

        # Valider le niveau de compétence (exemple : entre 1 et 5)
        if niveau and (niveau < 1 or niveau > 5):
            raise ValidationError("Le niveau de compétence doit être compris entre 1 et 5.")

        # Vérifier que l'employé n'a pas déjà cette compétence
        if NiveauCompetence.objects.filter(competence=competence, employe=employe).exists():
            raise ValidationError("Cet employé a déjà cette compétence avec le même niveau.")

        return cleaned_data
