# Generated by Django 4.2.17 on 2025-04-03 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpandraharaha', '0011_alter_mpandray_karatra_alter_mpiangona_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpandray',
            name='karatra',
            field=models.CharField(blank=True, help_text='V-0000 na L-0000', max_length=6, null=True, validators=[django.core.validators.RegexValidator('^[V|L]-\\d\\d\\d\\d', message="Atao mitovy amin'ny ohatra eo ambany io azafady")]),
        ),
    ]
