# Generated by Django 4.2.17 on 2025-04-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_bio_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=1, upload_to='profile'),
            preserve_default=False,
        ),
    ]
