# Generated by Django 4.1 on 2024-03-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0019_remove_contrat_contrat_doc_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contrat",
            name="prime_lait",
            field=models.FloatField(default=0, null=True),
        ),
    ]