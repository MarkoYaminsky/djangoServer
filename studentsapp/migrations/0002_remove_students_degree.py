# Generated by Django 4.0.3 on 2022-04-11 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='degree',
        ),
    ]
