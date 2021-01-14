# Generated by Django 3.1.2 on 2020-12-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20201207_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
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
