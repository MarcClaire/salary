# Generated by Django 4.2.7 on 2024-01-25 06:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0007_alter_paiement_annee_alter_paiement_mois"),
    ]

    operations = [
        migrations.AlterField(
            model_name="structure",
            name="telephone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
    ]