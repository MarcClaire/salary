# Generated by Django 4.1 on 2024-03-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0020_alter_contrat_prime_lait"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contrat",
            name="indemnite_fonction",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="indemnite_logement",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="indemnite_risque",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="indemnite_transport",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="nombre_annee_travail",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="prime_anciennete",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="prime_astreinte",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="prime_nourriture",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="contrat",
            name="prime_salissure",
            field=models.FloatField(default=0, null=True),
        ),
    ]
