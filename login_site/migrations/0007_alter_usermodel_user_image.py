# Generated by Django 3.2.4 on 2021-07-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_site', '0006_alter_usermodel_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(upload_to='user_image'),
        ),
    ]
