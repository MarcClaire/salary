# Generated by Django 4.2.7 on 2024-01-15 15:17

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categorie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "categorie",
                    models.CharField(
                        choices=[
                            ("Technicien", "Technicien"),
                            ("Ingénieur", "Ingénieur"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contrat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description_poste", models.TextField()),
                ("description_profil", models.TextField()),
                ("lieu_affectation", models.CharField(max_length=255)),
                ("cadre", models.BooleanField(default=False)),
                ("date_debut", models.DateField(default=0)),
                ("date_fin", models.DateField(default=0)),
                ("salaire_base", models.FloatField(default=0)),
                ("indemnite_logement", models.FloatField(default=0)),
                ("indemnite_transport", models.FloatField(default=0)),
                ("indemnite_fonction", models.FloatField(default=0)),
                ("prime_nourritur", models.FloatField(default=0)),
                ("prime_lait", models.FloatField(default=0)),
                ("prime_silissure", models.FloatField(default=0)),
                ("nombre_annee_travail", models.IntegerField(default=0)),
                ("prime_anciennete", models.BooleanField(default=False)),
                ("prime_quart", models.BooleanField(default=False)),
                ("prime_panier", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Diplome",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "diplome",
                    models.CharField(
                        choices=[
                            (
                                "Certificat d'Edude Primaire",
                                "Certificat d'Edude Primaire",
                            ),
                            (
                                "Brevet d'Etude du Premier Cycle",
                                "Brevet d'Etude du Premier Cycle",
                            ),
                            (
                                "Certificat de Qualification professionnelle",
                                "Certificat de Qualification professionnelle",
                            ),
                            (
                                "Brevet d'Etude Professionnelle",
                                "Brevet d'Etude Professionnelle",
                            ),
                            (
                                "Certificat d'Aptitude Professionnelle",
                                "Certificat d'Aptitude Professionnelle",
                            ),
                            ("Baccalauriat", "Baccalauriat"),
                            ("Licence", "Licence"),
                            ("Master", "Master"),
                            ("Doctorat", "Doctorat"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ModeCalcule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mode_calcul",
                    models.CharField(
                        choices=[
                            ("PARTICULIER", "PARTICULIER"),
                            ("CLASSIQUE", "CLASSIQUE"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Paiement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("salaire_net", models.FloatField(null=True)),
                ("salaire_brut", models.FloatField(null=True)),
                ("salaire_base", models.FloatField(null=True)),
                ("cotitsation_cnss", models.FloatField(null=True)),
                ("cnss_patronal", models.FloatField(null=True)),
                ("iuts", models.FloatField(null=True)),
                ("surplus_salaire", models.FloatField(null=True)),
                ("relicat_salaire", models.FloatField(null=True)),
                ("periode", models.CharField(max_length=20, null=True)),
                ("payer", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "contrat",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employe.contrat",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SituationMatrimoniale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "situation_matrimoniale",
                    models.CharField(
                        choices=[
                            ("Marié", "Marié"),
                            ("Célibataire", "Célibataire"),
                            ("Veuve", "Veuve"),
                            ("Veuf", "Veuf"),
                            ("Divorcé", "Divorcé"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Specialite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specialite",
                    models.CharField(
                        choices=[
                            ("Mathématique", "Mathématique"),
                            ("Chimie", "Chimie"),
                            ("Droit", "Droit"),
                            ("Resource Humaine", "Resource Humaine"),
                            ("Gestion Commerciale", "Gestion Commerciale"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Structure",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("denomination", models.CharField(max_length=255)),
                ("description_structure", models.TextField()),
                ("telephone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("adresse", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TypeContrat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type_contrat",
                    models.CharField(
                        choices=[
                            ("CDD", "Contrat à Durée Déterminé"),
                            ("CDI", "Contrat à Durée Indéterminé"),
                        ],
                        max_length=3,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pointage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nb_h_normal", models.IntegerField(null=True)),
                ("nb_h_15", models.IntegerField(null=True)),
                ("nb_h_35", models.IntegerField(null=True)),
                ("nb_h_50", models.IntegerField(null=True)),
                ("nb_h_60", models.IntegerField(null=True)),
                ("nb_h_120", models.IntegerField(null=True)),
                ("nb_quart", models.IntegerField(null=True)),
                ("nb_jour", models.IntegerField(null=True)),
                (
                    "paiement",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employe.paiement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("prenoms", models.CharField(max_length=255)),
                ("lieu_naissance", models.CharField(max_length=255)),
                ("date_naissance", models.DateField()),
                (
                    "sexe",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Féminin")], max_length=10
                    ),
                ),
                ("nombre_enfant", models.IntegerField()),
                (
                    "telephone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("adresse", models.CharField(max_length=255)),
                ("option", models.CharField(max_length=255)),
                ("cv", models.FileField(blank=True, null=True, upload_to="cvs/")),
                (
                    "lettre_motivation",
                    models.FileField(
                        blank=True, null=True, upload_to="lettres_motivation/"
                    ),
                ),
                (
                    "diplome",
                    models.FileField(blank=True, null=True, upload_to="diplomes/"),
                ),
                ("numero_cnss", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "numero_matricule",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "categorie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employe.categorie",
                    ),
                ),
                (
                    "dernier_diplome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employe.diplome",
                    ),
                ),
                (
                    "situation_matrimoniale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employe.situationmatrimoniale",
                    ),
                ),
                (
                    "specialite",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employe.specialite",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contrat",
            name="diplome_requis",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employe.diplome"
            ),
        ),
        migrations.AddField(
            model_name="contrat",
            name="employe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employe.employe"
            ),
        ),
        migrations.AddField(
            model_name="contrat",
            name="mode_calcul",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employe.modecalcule"
            ),
        ),
        migrations.AddField(
            model_name="contrat",
            name="structure",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employe.structure"
            ),
        ),
        migrations.AddField(
            model_name="contrat",
            name="type_contrat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employe.typecontrat"
            ),
        ),
    ]
