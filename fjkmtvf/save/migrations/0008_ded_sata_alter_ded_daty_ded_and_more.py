# Generated by Django 4.2.17 on 2025-04-11 14:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tetibola', '0007_ded_mpitantsorabola'),
    ]

    operations = [
        migrations.AddField(
            model_name='ded',
            name='sata',
            field=models.CharField(choices=[('en_cours', 'En cours'), ('valide', 'Validé')], default='en_cours', max_length=10),
        ),
        migrations.AlterField(
            model_name='ded',
            name='daty_ded',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Daty nanaovana DED'),
        ),
        migrations.AlterField(
            model_name='ded',
            name='mpitantsorabola',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mpitantsorabola', to=settings.AUTH_USER_MODEL, verbose_name='Mpitantsoratry ny vola'),
        ),
        migrations.AlterField(
            model_name='ded',
            name='num_ded',
            field=models.CharField(max_length=3, verbose_name='DED'),
        ),
        migrations.CreateModel(
            name='Fanamarinana_ded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ded', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tetibola.ded')),
                ('mpanamarina_birao_ssa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mpanamarina_toby_ssa', to=settings.AUTH_USER_MODEL)),
                ('mpanamarina_birao_tvf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mpanamarina_birao_tvf', to=settings.AUTH_USER_MODEL)),
                ('mpanamarina_toby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mpanamarina_toby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
