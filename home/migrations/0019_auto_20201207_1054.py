# Generated by Django 3.1.2 on 2020-12-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20201207_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='subjects',
            field=models.ManyToManyField(to='home.Subjects'),
        ),
        migrations.AlterField(
            model_name='file',
            name='link_url',
            field=models.URLField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ManyToManyField(to='home.Exam'),
        ),
    ]
