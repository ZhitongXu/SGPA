# Generated by Django 3.1.1 on 2020-09-25 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Poj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('硕博连读', '硕博连读'), ('直博', '直博'), ('专硕', '专硕')], max_length=100, null=True, verbose_name='入学类型')),
                ('enteryear', models.IntegerField(blank=True, max_length=5, null=True, verbose_name='入学年份')),
                ('teafield', models.CharField(blank=True, choices=[('数据科学', '数据科学'), ('数理统计', '数理统计'), ('经济社会统计', '经济社会统计'), ('风险管理与精算', '风险管理与精算'), ('生物卫生医学统计', '生物卫生医学统计')], max_length=100, null=True, verbose_name='导师方向')),
                ('othercourses', models.TextField(blank=True, null=True, verbose_name='其他课程')),
                ('gpa', models.FloatField(blank=True, null=True, verbose_name='本科GPA')),
                ('gpatotal', models.IntegerField(blank=True, null=True, verbose_name='本科GPA满分')),
                ('selfassessment', models.IntegerField(blank=True, choices=[(5, '完全掌握'), (4, '熟练'), (3, '还可以'), (1, '一般'), (-5, '薄弱')], max_length=100, null=True, verbose_name='知识掌握程度')),
                ('otherpoj', models.TextField(blank=True, null=True, verbose_name='其他项目经历')),
                ('goal', models.IntegerField(blank=True, choices=[(1, '完成硕士生基本要求拿到学位'), (2, '在完成硕士生基本要求拿到学位的基础上在导师指导下完成一篇高质量的硕士论文，并获得老师的认可'), (3, '在前两个目标的基础上，为获得国内一流大学博士学位做好准备，打好基础'), (4, '在前两个目标的基础上，为获得国际一流大学博士学位做好准备，打好基础')], null=True, verbose_name='阶段性目标')),
                ('courses', models.ManyToManyField(blank=True, null=True, to='sgpa.Course', verbose_name='课程选择')),
                ('poj', models.ManyToManyField(blank=True, null=True, to='sgpa.Poj', verbose_name='项目经历')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
