from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from employe.models import Employe, SecteurActivite
from django.db.models import Count

def gpec_dashboard(request):
    return render(request, 'gpec/dashboard.html')

def evaluation(request):
    evaluations = Evaluation.objects.all()
    return render(request, 'gpec/liste_evaluations.html', {'evaluations': evaluations})

def gestion_talents(request):
    talents = Talent.objects.all()
    return render(request, 'gpec/gestion_talents.html', {'talents': talents})

def ajouter_talent(request):
    if request.method == 'POST':
        form = TalentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Talent ajouté avec succès.")
            return redirect('gestion_talents')
    else:
        form = TalentForm()
    return render(request, 'gpec/talent_form.html', {'form': form})

def modifier_talent(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)
    if request.method == 'POST':
        form = TalentForm(request.POST, instance=talent)
        if form.is_valid():
            form.save()
            messages.success(request, "Talent modifié avec succès.")
            return redirect('gestion_talents')
    else:
        form = TalentForm(instance=talent)
    return render(request, 'gpec/talent_form.html', {'form': form})

def ajouter_performance(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            performance = form.save(commit=False)
            performance.talent = talent
            performance.save()
            messages.success(request, "Performance ajoutée avec succès.")
            return redirect('gestion_talents')
    else:
        form = PerformanceForm(initial={'talent': talent})
    return render(request, 'gpec/performance_form.html', {'form': form, 'talent': talent})

def detail_talent(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)
    performances = talent.performances.all().order_by('-date_evaluation')
    return render(request, 'gpec/detail_talent.html', {'talent': talent, 'performances': performances})


# def dossier_personnel(request):
#     dossiers = DossierPersonnel.objects.all()
#     return render(request, 'gpec/dossier_personnel.html', {'dossiers': dossiers})
def dossier_personnel(request):
    employes = Employe.objects.all()
    return render(request, 'gpec/dossier_personnel.html', {'employes': employes})

def detail_dossier(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    documents = employe.documents.all().order_by('-date_ajout')
    return render(request, 'gpec/detail_dossier.html', {'employe': employe, 'documents': documents})

def ajouter_document(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    if request.method == 'POST':
        form = DocumentPersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.employe = employe
            document.save()
            messages.success(request, "Document ajouté avec succès.")
            return redirect('detail_dossier', employe_id=employe.id)
    else:
        form = DocumentPersonnelForm(initial={'employe': employe})
    return render(request, 'gpec/ajouter_document.html', {'form': form, 'employe': employe})

def supprimer_document(request, document_id):
    document = get_object_or_404(DocumentPersonnel, id=document_id)
    employe_id = document.employe.id
    if request.method == 'POST':
        document.delete()
        messages.success(request, "Document supprimé avec succès.")
        return redirect('detail_dossier', employe_id=employe_id)
    return render(request, 'gpec/confirmer_suppression.html', {'document': document})

#Effectifs start
def effectifs_par_genre_et_secteur(request):
    secteurs = SecteurActivite.objects.all()
    genre_selectionne = request.GET.get('sexe')
    secteur_selectionne = request.GET.get('secteur')

    effectifs = Employe.objects.all()

    if genre_selectionne:
        effectifs = effectifs.filter(genre=genre_selectionne)

    if secteur_selectionne:
        effectifs = effectifs.filter(secteur_activite_id=secteur_selectionne)

    effectifs_par_secteur = effectifs.values('secteur_activite__nom', 'sexe').annotate(
        total=Count('id')
    ).order_by('secteur_activite__nom', 'sexe')

    context = {
        'secteurs': secteurs,
        'genre_selectionne': genre_selectionne,
        'secteur_selectionne': secteur_selectionne,
        'effectifs_par_secteur': effectifs_par_secteur,
        'total_effectifs': effectifs.count(),
    }

    return render(request, 'gpec/effectifs_genre_secteur.html', context)

# def effectifs(request):
#     employes = Employe.objects.all()
#     return render(request, 'gpec/effectifs.html', {'employes': employes})

def suivi_carriere(request):
    evolutions = EvolutionCarriere.objects.all().order_by('-date_changement')
    mouvements = MouvementPersonnel.objects.all().order_by('-date_mouvement')
    context = {
        'evolutions': evolutions,
        'mouvements': mouvements,
    }
    return render(request, 'gpec/suivi_carriere.html', context)

def ajouter_evolution(request):
    if request.method == 'POST':
        form = EvolutionCarriereForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Évolution de carrière ajoutée avec succès.")
            return redirect('suivi_carriere')
    else:
        form = EvolutionCarriereForm()
    return render(request, 'gpec/ajouter_evolution.html', {'form': form})

def ajouter_mouvement(request):
    if request.method == 'POST':
        form = MouvementPersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mouvement de personnel ajouté avec succès.")
            return redirect('suivi_carriere')
    else:
        form = MouvementPersonnelForm()
    return render(request, 'gpec/ajouter_mouvement.html', {'form': form})

def detail_employe_carriere(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    evolutions = employe.evolutions_carriere.all().order_by('-date_changement')
    mouvements = employe.mouvements.all().order_by('-date_mouvement')
    context = {
        'employe': employe,
        'evolutions': evolutions,
        'mouvements': mouvements,
    }
    return render(request, 'gpec/detail_employe_carriere.html', context)


# def suivi_carriere(request):
#     suivis = SuiviCarriere.objects.all()
#     return render(request, 'gpec/suivi_carriere.html', {'suivis': suivis})

# def plan_recrutement(request):
#     plans = PlanRecrutement.objects.all()
#     return render(request, 'gpec/plan_recrutement.html', {'plans': plans})

def liste_plans_recrutement(request):
    plans = PlanRecrutement.objects.all().order_by('-date_debut')
    return render(request, 'gpec/liste_plans_recrutement.html', {'plans': plans})

def ajouter_plan_recrutement(request):
    if request.method == 'POST':
        form = PlanRecrutementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan de recrutement ajouté avec succès.")
            return redirect('liste_plans_recrutement')
    else:
        form = PlanRecrutementForm()
    return render(request, 'gpec/ajouter_plan_recrutement.html', {'form': form})

def detail_plan_recrutement(request, plan_id):
    plan = get_object_or_404(PlanRecrutement, id=plan_id)
    candidats = plan.candidats.all().order_by('-date_candidature')
    return render(request, 'gpec/detail_plan_recrutement.html', {'plan': plan, 'candidats': candidats})

def ajouter_candidat(request, plan_id):
    plan = get_object_or_404(PlanRecrutement, id=plan_id)
    if request.method == 'POST':
        form = CandidatPlanForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save(commit=False)
            candidat.plan = plan
            candidat.save()
            messages.success(request, "Candidat ajouté avec succès.")
            return redirect('detail_plan_recrutement', plan_id=plan.id)
    else:
        form = CandidatPlanForm(initial={'plan': plan})
    return render(request, 'gpec/ajouter_candidat.html', {'form': form, 'plan': plan})

def modifier_statut_candidat(request, candidat_id):
    candidat = get_object_or_404(CandidatPlan, id=candidat_id)
    if request.method == 'POST':
        nouveau_statut = request.POST.get('statut')
        if nouveau_statut in dict(CandidatPlan.STATUT_CHOICES):
            candidat.statut = nouveau_statut
            candidat.save()
            messages.success(request, "Statut du candidat mis à jour.")
        else:
            messages.error(request, "Statut invalide.")
    return redirect('detail_plan_recrutement', plan_id=candidat.plan.id)


# def gestion_temps(request):
#     pointages = PointagePresence.objects.all()
#     return render(request, 'gpec/gestion_temps.html', {'pointages': pointages})
def gestion_temps_travail(request):
    aujourd_hui = timezone.now().date()
    pointages = Pointage.objects.filter(date=aujourd_hui).order_by('employe__nom')
    absences = Absence.objects.filter(date_debut__lte=aujourd_hui, date_fin__gte=aujourd_hui).order_by('employe__nom')
    return render(request, 'gpec/gestion_temps_travail.html', {'pointages': pointages, 'absences': absences})

def ajouter_pointage(request):
    if request.method == 'POST':
        form = PointageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pointage ajouté avec succès.")
            return redirect('gestion_temps_travail')
    else:
        form = PointageForm(initial={'date': timezone.now().date()})
    return render(request, 'gpec/ajouter_pointage.html', {'form': form})

def modifier_pointage(request, pointage_id):
    pointage = get_object_or_404(Pointage, id=pointage_id)
    if request.method == 'POST':
        form = PointageForm(request.POST, instance=pointage)
        if form.is_valid():
            form.save()
            messages.success(request, "Pointage modifié avec succès.")
            return redirect('gestion_temps_travail')
    else:
        form = PointageForm(instance=pointage)
    return render(request, 'gpec/modifier_pointage.html', {'form': form})

def ajouter_absence(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Absence ajoutée avec succès.")
            return redirect('gestion_temps_travail')
    else:
        form = AbsenceForm()
    return render(request, 'gpec/ajouter_absence.html', {'form': form})

def rapport_temps_travail(request):
    employes = Employe.objects.all()
    debut = request.GET.get('debut')
    fin = request.GET.get('fin')
    
    if debut and fin:
        pointages = Pointage.objects.filter(date__range=[debut, fin]).order_by('employe', 'date')
        absences = Absence.objects.filter(date_debut__lte=fin, date_fin__gte=debut).order_by('employe', 'date_debut')
    else:
        pointages = Absence.objects.none()
        absences = Absence.objects.none()
    
    return render(request, 'gpec/rapport_temps_travail.html', {
        'employes': employes,
        'pointages': pointages,
        'absences': absences,
        'debut': debut,
        'fin': fin,
    })

# def fiches_postes(request):
#     fiches = FichePoste.objects.all()
#     return render(request, 'gpec/fiches_postes.html', {'fiches': fiches})
def liste_fiches_poste(request):
    fiches = FichePoste.objects.all().order_by('titre')
    return render(request, 'gpec/liste_fiches_poste.html', {'fiches': fiches})

def ajouter_fiche_poste(request):
    if request.method == 'POST':
        form = FichePosteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fiche de poste ajoutée avec succès.")
            return redirect('liste_fiches_poste')
    else:
        form = FichePosteForm()
    return render(request, 'gpec/ajouter_fiche_poste.html', {'form': form})

def detail_fiche_poste(request, fiche_id):
    fiche = get_object_or_404(FichePoste, id=fiche_id)
    employes = EmployePoste.objects.filter(fiche_poste=fiche)
    return render(request, 'gpec/detail_fiche_poste.html', {'fiche': fiche, 'employes': employes})

def modifier_fiche_poste(request, fiche_id):
    fiche = get_object_or_404(FichePoste, id=fiche_id)
    if request.method == 'POST':
        form = FichePosteForm(request.POST, instance=fiche)
        if form.is_valid():
            form.save()
            messages.success(request, "Fiche de poste modifiée avec succès.")
            return redirect('detail_fiche_poste', fiche_id=fiche.id)
    else:
        form = FichePosteForm(instance=fiche)
    return render(request, 'gpec/modifier_fiche_poste.html', {'form': form, 'fiche': fiche})

def attribuer_poste(request):
    if request.method == 'POST':
        form = EmployePosteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Poste attribué avec succès.")
            return redirect('liste_fiches_poste')
    else:
        form = EmployePosteForm()
    return render(request, 'gpec/attribuer_poste.html', {'form': form})

# def referentiel_competences(request):
#     competences = ReferentielCompetences.objects.all()
#     return render(request, 'gpec/referentiel_competences.html', {'competences': competences})
def liste_competences(request):
    competences = Competence.objects.all().order_by('categorie', 'nom')
    return render(request, 'gpec/liste_competences.html', {'competences': competences})

def ajouter_competence(request):
    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compétence ajoutée avec succès.")
            return redirect('liste_competences')
    else:
        form = CompetenceForm()
    return render(request, 'gpec/ajouter_competence.html', {'form': form})

def modifier_competence(request, competence_id):
    competence = get_object_or_404(Competence, id=competence_id)
    if request.method == 'POST':
        form = CompetenceForm(request.POST, instance=competence)
        if form.is_valid():
            form.save()
            messages.success(request, "Compétence modifiée avec succès.")
            return redirect('liste_competences')
    else:
        form = CompetenceForm(instance=competence)
    return render(request, 'gpec/modifier_competence.html', {'form': form, 'competence': competence})

def evaluer_competence(request):
    if request.method == 'POST':
        form = NiveauCompetenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Évaluation de compétence enregistrée avec succès.")
            return redirect('liste_competences')
    else:
        form = NiveauCompetenceForm()
    return render(request, 'gpec/evaluer_competence.html', {'form': form})

def profil_competences_employe(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    niveaux_competences = NiveauCompetence.objects.filter(employe=employe).order_by('competence__categorie', 'competence__nom')
    return render(request, 'gpec/profil_competences_employe.html', {'employe': employe, 'niveaux_competences': niveaux_competences})

def matrice_competences(request):
    competences = Competence.objects.all().order_by('categorie', 'nom')
    employes = Employe.objects.all().order_by('nom')
    matrice = {}
    for employe in employes:
        matrice[employe] = {}
        for competence in competences:
            try:
                niveau = NiveauCompetence.objects.get(employe=employe, competence=competence)
                matrice[employe][competence] = niveau.niveau
            except NiveauCompetence.DoesNotExist:
                matrice[employe][competence] = 0
    return render(request, 'gpec/matrice_competences.html', {'competences': competences, 'employes': employes, 'matrice': matrice})


def evaluation_add(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluation')
    else:
        form = EvaluationForm()
    return render(request, 'gpec/ajouter_evaluation.html', {'form': form})

# def liste_evaluations(request):
#     evaluations = Evaluation.objects.all()
#     return render(request, 'gpec/liste_evaluations.html', {'evaluations': evaluations})
