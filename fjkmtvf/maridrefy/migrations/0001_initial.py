# Generated by Django 4.2.17 on 2025-04-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sondage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous', models.ImageField(unique=True, upload_to='')),
            ],
        ),
    ]
