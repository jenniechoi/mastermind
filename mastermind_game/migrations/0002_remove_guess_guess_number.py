# Generated by Django 2.2.6 on 2020-01-28 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind_game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guess',
            name='guess_number',
        ),
    ]
