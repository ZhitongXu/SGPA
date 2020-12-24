# Generated by Django 3.1.1 on 2020-09-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ball', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='type',
            field=models.CharField(blank=True, choices=[('level1', 'level1'), ('level21', 'level21'), ('model selection', 'model selection'), ('machine learning', 'machine learning'), ('theoretic statistics', 'theoretic statistics'), ('bayesian inference', 'bayesian inference'), ('bio statistics', 'bio statistics'), ('mm', 'mm'), ('level23', 'level23'), ('level3', 'level3')], max_length=500, null=True, verbose_name='关键词分类'),
        ),
    ]
