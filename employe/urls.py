from django.urls import path
from employe.views import index, liste, ajouter_employe, update_empl_data,delete_employe, form,ajouter_contrat,liste_contrat,update_contrat_data
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('personel',views.liste, name='personel'),
    path('update_empl_data/<int:id>',views.update_empl_data, name='updateemploye'),
    path('delete_employe/<int:id>',views.delete_employe, name='deleteemploye'),
    path('form',views.form, name='form'),
    path('add_employe',views.ajouter_employe, name='add_employe'),
    path('contrat',views.liste_contrat, name='contrat'),
    path('update_contrat_data/<int:id>',views.update_contrat_data, name='update_contrat'),
    path('delete_contrat/<int:id>',views.delete_contrat, name='deletecontrat'),
    path('add_contrat',views.ajouter_contrat, name='add_contrat'),

]