# Generated by Django 4.2.17 on 2025-04-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpandraharaha', '0035_alter_mpiangona_daty_nahaterahana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ankohonana',
            name='ankid',
        ),
        migrations.RemoveField(
            model_name='mpandray',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='mpiangona',
            name='piid',
        ),
        migrations.RemoveField(
            model_name='mpikambana',
            name='pikid',
        ),
        migrations.RemoveField(
            model_name='tossaafiko',
            name='said',
        ),
    ]
