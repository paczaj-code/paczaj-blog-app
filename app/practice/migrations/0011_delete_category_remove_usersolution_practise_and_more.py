# Generated by Django 4.0.6 on 2022-07-24 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0010_usersolution_is_public'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='usersolution',
            name='practise',
        ),
        migrations.RemoveField(
            model_name='usersolution',
            name='user',
        ),
        migrations.DeleteModel(
            name='Practice',
        ),
        migrations.DeleteModel(
            name='UserSolution',
        ),
    ]