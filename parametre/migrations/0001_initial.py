# Generated by Django 4.2.7 on 2024-01-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JourFerier",
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
                ("libelle", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("description", models.TextField()),
            ],
            options={
                "db_table": "jour_ferier",
            },
        ),
        migrations.CreateModel(
            name="Nuit",
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
                ("est_nuit", models.BooleanField()),
                ("min", models.IntegerField()),
            ],
            options={
                "db_table": "nuit_table",
            },
        ),
        migrations.CreateModel(
            name="TarifHeureSup",
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
                    "taux",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("jourFerie", models.BooleanField(default=False)),
                ("nuit", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "tarif_heure_sup",
            },
        ),
        migrations.CreateModel(
            name="Taxe",
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
                ("libelle", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
            options={
                "db_table": "taxe_table",
            },
        ),
    ]
