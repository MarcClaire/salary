from django.urls import path
from . import views

urlpatterns = [
    path('gpec/dash/', views.gpec_dashboard, name='gpec_dashboard'),

    path('gpec/evaluation/', views.evaluation, name='evaluation'),
    path('gpec/ajout-evaluation/', views.evaluation_add, name='evaluation_add'),

    #path('gpec/evaluations/', views.liste_evaluations, name='liste_evaluations'),
    path('gpec/gestion-talents/', views.gestion_talents, name='gestion_talents'),
    path('gpec/ajouter-talent/', views.ajouter_talent, name='ajouter_talent'),
    path('gpec/modifier-talent/<int:talent_id>/', views.modifier_talent, name='modifier_talent'),
    path('gpec/ajouter-performance/<int:talent_id>/', views.ajouter_performance, name='ajouter_performance'),
    path('gpec/detail-talent/<int:talent_id>/', views.detail_talent, name='detail_talent'),

    #path('gpec/dossier-personnel/', views.dossier_personnel, name='dossier_personnel'),
    path('gpec/dossier-personnel/', views.dossier_personnel, name='dossier_personnel'),
    path('gpec/detail-dossier/<int:employe_id>/', views.detail_dossier, name='detail_dossier'),
    path('gpec/ajouter-document/<int:employe_id>/', views.ajouter_document, name='ajouter_document'),
    path('gpec/supprimer-document/<int:document_id>/', views.supprimer_document, name='supprimer_document'),

    #Effectifs
    path('gpec/effectifs/', views.effectifs_par_genre_et_secteur, name='effectifs_par_genre_et_secteur'),

    # path('gpec/effectifs/', views.effectifs, name='effectifs'),

    # path('gpec/suivi-carriere/', views.suivi_carriere, name='suivi_carriere'),
    path('gpec/suivi-carriere/', views.suivi_carriere, name='suivi_carriere'),
    path('gpec/ajouter-evolution/', views.ajouter_evolution, name='ajouter_evolution'),
    path('gpec/ajouter-mouvement/', views.ajouter_mouvement, name='ajouter_mouvement'),
    path('gpec/detail-employe-carriere/<int:employe_id>/', views.detail_employe_carriere, name='detail_employe_carriere'),

    #path('gpec/plan-recrutement/', views.plan_recrutement, name='plan_recrutement'),
    path('gpec/plans-recrutement/', views.liste_plans_recrutement, name='liste_plans_recrutement'),
    path('gpec/ajouter-plan-recrutement/', views.ajouter_plan_recrutement, name='ajouter_plan_recrutement'),
    path('gpec/plan-recrutement/<int:plan_id>/', views.detail_plan_recrutement, name='detail_plan_recrutement'),
    path('gpec/ajouter-candidat/<int:plan_id>/', views.ajouter_candidat, name='ajouter_candidat'),
    path('gpec/modifier-statut-candidat/<int:candidat_id>/', views.modifier_statut_candidat, name='modifier_statut_candidat'),


    # path('gpec/gestion-temps/', views.gestion_temps, name='gestion_temps'),
    path('gpec/gestion-temps-travail/', views.gestion_temps_travail, name='gestion_temps_travail'),
    path('gpec/ajouter-pointage/', views.ajouter_pointage, name='ajouter_pointage'),
    path('gpec/modifier-pointage/<int:pointage_id>/', views.modifier_pointage, name='modifier_pointage'),
    path('gpec/ajouter-absence/', views.ajouter_absence, name='ajouter_absence'),
    path('gpec/rapport-temps-travail/', views.rapport_temps_travail, name='rapport_temps_travail'),

    #path('gpec/fiches-postes/', views.fiches_postes, name='fiches_postes'),
    path('gpec/fiches-poste/', views.liste_fiches_poste, name='liste_fiches_poste'),
    path('gpec/ajouter-fiche-poste/', views.ajouter_fiche_poste, name='ajouter_fiche_poste'),
    path('gpec/fiche-poste/<int:fiche_id>/', views.detail_fiche_poste, name='detail_fiche_poste'),
    path('gpec/modifier-fiche-poste/<int:fiche_id>/', views.modifier_fiche_poste, name='modifier_fiche_poste'),
    path('gpec/attribuer-poste/', views.attribuer_poste, name='attribuer_poste'),


    #path('gpec/referentiel-competences/', views.referentiel_competences, name='referentiel_competences'),
    path('gpec/competences/', views.liste_competences, name='liste_competences'),
    path('gpec/ajouter-competence/', views.ajouter_competence, name='ajouter_competence'),
    path('gpec/modifier-competence/<int:competence_id>/', views.modifier_competence, name='modifier_competence'),
    path('gpec/evaluer-competence/', views.evaluer_competence, name='evaluer_competence'),
    path('gpec/profil-competences/<int:employe_id>/', views.profil_competences_employe, name='profil_competences_employe'),
    path('gpec/matrice-competences/', views.matrice_competences, name='matrice_competences'),

]
