# Generated by Django 4.0.6 on 2022-07-23 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminology', '0002_term_slug_alter_term_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='term',
            name='slug',
        ),
    ]
