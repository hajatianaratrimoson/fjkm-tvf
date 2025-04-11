# Generated by Django 4.2.17 on 2025-04-11 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tetibola', '0002_remove_diarimbola_daty_alter_rafitra_axe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diarimbola',
            name='laminasa',
        ),
        migrations.AddField(
            model_name='ded',
            name='laminasa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diarimbola_laminasa', to='tetibola.laminasa'),
        ),
    ]
