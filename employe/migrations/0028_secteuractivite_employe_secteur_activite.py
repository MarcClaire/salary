# Generated by Django 4.2.16 on 2024-09-20 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0027_contrat_nature_revenu_contrat_type_personnel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecteurActivite",
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
                ("nom", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="employe",
            name="secteur_activite",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="employe.secteuractivite",
            ),
        ),
    ]
