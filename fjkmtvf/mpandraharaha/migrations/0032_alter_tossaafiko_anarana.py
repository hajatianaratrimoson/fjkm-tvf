# Generated by Django 4.2.17 on 2025-04-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpandraharaha', '0031_alter_mpikambana_andraikitra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tossaafiko',
            name='anarana',
            field=models.CharField(choices=[('stk', 'STK'), ('ssa', 'SSA'), ('fdl', 'FDL'), ('aam', 'AAM'), ('safif', 'SAFIF'), ('fafi', 'FAFI'), ('fmo', 'FMO'), ('svm', 'SVM'), ('dorkasy', 'DORKASY'), ('vfl', 'VFL'), ('zr', 'ZR'), ('sampati', 'SAMPATI'), ('amboarampeo', 'AMBOARAMPEO'), ('aff', 'AFF'), ('kpsv', 'KPSV'), ('kga', 'KGA'), ('kff', 'KFF'), ('kvo', 'KVO'), ('kftl', 'KFTL'), ('kmb', 'KMB'), ('tpram', 'TPRAM'), ('toby_fifaliana', 'TOBY FIFALIANA'), ('toby_fitiavana', 'TOBY FITIAVANA'), ('toby_fahamarinana', 'TOBY FAHAMARINANA'), ('toby_fiadanana', 'TOBY FIADANANA')], default='ssa', error_messages={'required': 'Efa misy io anarana io'}, help_text="Anarana oentin'ny Tossaafiko", max_length=17, unique=True, verbose_name='tossaafiko'),
        ),
    ]
