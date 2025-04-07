# Generated by Django 4.2.17 on 2025-04-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpandraharaha', '0017_tossaafiko_delete_sampana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tossaafiko',
            name='anarana',
            field=models.CharField(choices=[('stk', 'STK'), ('ssa', 'SSA'), ('fdl', 'FDL'), ('toby_fifaliana', 'Toby Fifaliana'), ('toby_fitiavana', 'Toby Fitiavana'), ('toby_fahamarinana', 'Toby Fahamarinana'), ('toby_fiadanana', 'Toby Fiadanana')], default='ssa', max_length=17, verbose_name='tossaafiko'),
        ),
        migrations.AlterField(
            model_name='tossaafiko',
            name='andraikitra',
            field=models.CharField(choices=[('filoha', 'Filoha'), ('filoha_mpanampy', 'Filoha Mpanampy'), ('tonia', 'Mpitan-tsoratry ny fivoriana'), ('tonia_vola', 'Mpitan-tsoratry ny vola'), ('mpitahiry_vola', 'Mpitahiry Vola'), ('mpanolo_tsaina', 'Mpanolo-tsaina'), ('mpiakambana', 'Mpikambana')], default='filoha', max_length=15),
        ),
    ]
