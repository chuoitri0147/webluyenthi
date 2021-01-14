# Generated by Django 3.1.2 on 2021-01-14 15:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20210114_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subjects',
            field=models.ManyToManyField(to='home.Subjects'),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ManyToManyField(to='home.Exam'),
        ),
    ]
