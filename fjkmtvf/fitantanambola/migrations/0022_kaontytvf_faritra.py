# Generated by Django 4.2.17 on 2025-05-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitantanambola", "0021_alter_journalcaisse_fanamarihana"),
    ]

    operations = [
        migrations.AddField(
            model_name="kaontytvf",
            name="faritra",
            field=models.CharField(
                blank=True,
                choices=[("ivelany", "Ivelany"), ("anatiny", "Anatiny")],
                max_length=10,
                null=True,
            ),
        ),
    ]
