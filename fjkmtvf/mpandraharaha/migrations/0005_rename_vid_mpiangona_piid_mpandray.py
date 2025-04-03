# Generated by Django 4.2.17 on 2025-03-27 09:40

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('mpandraharaha', '0004_alter_mpiangona_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpiangona',
            old_name='vid',
            new_name='piid',
        ),
        migrations.CreateModel(
            name='Mpandray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=30, prefix='pad', unique=True)),
                ('karatra', models.CharField(blank=True, max_length=8, null=True)),
                ('taona', models.DateField()),
                ('Fiangonana', models.CharField(max_length=50)),
                ('mpiangona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mpandraharaha.mpiangona')),
            ],
            options={
                'verbose_name_plural': 'Mpandray',
            },
        ),
    ]
