# Generated by Django 2.2.6 on 2020-01-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=4)),
                ('guess_number', models.IntegerField()),
            ],
        ),
    ]
