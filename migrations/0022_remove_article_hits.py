# Generated by Django 3.2.9 on 2022-03-08 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_article_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]
