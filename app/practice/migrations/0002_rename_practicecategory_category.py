# Generated by Django 4.0.6 on 2022-07-23 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PracticeCategory',
            new_name='Category',
        ),
    ]