# Generated by Django 3.2.9 on 2022-03-09 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleviews',
            old_name='create',
            new_name='created',
        ),
    ]
