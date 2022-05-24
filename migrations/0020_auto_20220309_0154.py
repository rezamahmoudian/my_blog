# Generated by Django 3.2.9 on 2022-03-08 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_article_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='blog.IP_Address', verbose_name='بازدید ها'),
        ),
        migrations.CreateModel(
            name='ArticleViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ip_address')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
    ]
