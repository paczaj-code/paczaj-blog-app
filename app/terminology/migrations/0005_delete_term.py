# Generated by Django 4.0.6 on 2022-07-23 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminology', '0004_term_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Term',
        ),
    ]