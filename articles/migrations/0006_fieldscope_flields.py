# Generated by Django 3.0.7 on 2020-06-24 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200624_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldscope',
            name='flields',
            field=models.ManyToManyField(through='articles.ArticleField', to='articles.Article'),
        ),
    ]
