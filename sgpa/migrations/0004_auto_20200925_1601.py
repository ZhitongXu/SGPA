# Generated by Django 3.1.1 on 2020-09-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgpa', '0003_auto_20200925_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ques',
            name='enteryear',
            field=models.IntegerField(blank=True, max_length=5, null=True, verbose_name='入学年份'),
        ),
    ]
