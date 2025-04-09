# Generated by Django 4.2.17 on 2025-04-08 19:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpandraharaha', '0040_remove_mpandray_mpiangona_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atolotra',
            old_name='zaza',
            new_name='atolotra',
        ),
        migrations.AddField(
            model_name='atolotra',
            name='daty',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Daty nanolorana'),
        ),
        migrations.CreateModel(
            name='Batisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daty', models.DateField(default=datetime.datetime.now, verbose_name='Daty batisa')),
                ('batisa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batisa_mpiangona', to='mpandraharaha.mpiangona', verbose_name="Anaran'ny zaza")),
                ('rad', models.ManyToManyField(blank=True, null=True, to='mpandraharaha.mpiangona')),
            ],
            options={
                'verbose_name_plural': 'Batisa',
            },
        ),
    ]
