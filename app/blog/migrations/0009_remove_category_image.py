# Generated by Django 4.0.6 on 2022-07-27 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_image_alter_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]