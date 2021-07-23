# Generated by Django 3.2.5 on 2021-07-22 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.CharField(max_length=10)),
                ('player2', models.CharField(max_length=10)),
                ('player3', models.CharField(max_length=10)),
                ('player4', models.CharField(max_length=10)),
                ('leader', models.CharField(max_length=10)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournamentsmodel')),
            ],
        ),
    ]
