# Generated by Django 2.2.6 on 2020-04-30 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mastermind_game', '0008_game_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='result',
            new_name='win',
        ),
        migrations.RenameField(
            model_name='guess',
            old_name='nums_right',
            new_name='correct_digits',
        ),
        migrations.RenameField(
            model_name='guess',
            old_name='places_right',
            new_name='correct_position',
        ),
    ]
