from django import forms
from .models import Employe, Contrat,SituationMatrimoniale,Diplome,Categorie,Specialite,Structure,TypeContrat

# Utilisez tous les champs du modèle Employe

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'  

    # Ajoutez des classes Bootstrap aux champs du formulaire
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenoms = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lieu_naissance = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sexe = forms.ChoiceField(choices=[('M', 'Masculin'), ('F', 'Féminin')], widget=forms.Select(attrs={'class': 'form-control'}))
    situation_matrimoniale = forms.ModelChoiceField(queryset=SituationMatrimoniale.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    nombre_enfant = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    adresse = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dernier_diplome = forms.ModelChoiceField(queryset=Diplome.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    specialite = forms.ModelChoiceField(queryset=Specialite.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cv = forms.FileField(widget=forms.FileInput( attrs={'class': 'form-control-file'}), required=False)
    lettre_motivation = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    diplome = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    numero_cnss = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    numero_matricule = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    date_naissance = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), input_formats=['%Y-%m-%d'])

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'
    # Ajoutez des classes Bootstrap aux champs du formulaire
    structure = forms.ModelChoiceField(queryset=Structure.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    employe = forms.ModelChoiceField(queryset=Employe.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    description_poste = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    description_profil = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    lieu_affectation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diplome_requis = forms.ModelChoiceField(queryset=Diplome.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    type_contrat = forms.ModelChoiceField(queryset=TypeContrat.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    date_debut = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), input_formats=['%Y-%m-%d'])
    date_fin = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), input_formats=['%Y-%m-%d'])

