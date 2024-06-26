# Generated by Django 4.1 on 2024-03-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0018_type_paiement_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contrat",
            name="contrat_doc",
        ),
        migrations.RemoveField(
            model_name="typecontrat",
            name="type_contrat",
        ),
        migrations.AddField(
            model_name="typecontrat",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="contrats/"),
        ),
        migrations.AddField(
            model_name="typecontrat",
            name="libelle",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name="ContratDoc",
        ),
    ]
