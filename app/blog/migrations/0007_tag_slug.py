# Generated by Django 4.0.6 on 2022-07-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_slug_alter_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
