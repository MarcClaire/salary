# Generated by Django 4.1 on 2024-01-16 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contrat",
            name="indemnite_risque",
            field=models.FloatField(default=0),
        ),
    ]
