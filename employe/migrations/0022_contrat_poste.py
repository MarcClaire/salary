# Generated by Django 4.1 on 2024-03-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0021_alter_contrat_indemnite_fonction_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contrat",
            name="poste",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
