# Generated by Django 4.1 on 2024-03-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calcul", "0008_parametre_calcul_nb_jour_travail_normal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parametre_calcul",
            name="nb_jour_travail_normal",
            field=models.IntegerField(null=True),
        ),
    ]
