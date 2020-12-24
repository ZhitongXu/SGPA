from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Poj(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Hardship(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Ques(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=settings.TYPE_CHOICES, verbose_name='入学类型', null=True, blank=True)
    enteryear = models.IntegerField(max_length=5, verbose_name='入学年份', null=True, blank=True)
    teafield = models.CharField(max_length=100, choices=settings.FIELD_CHOICES, verbose_name='导师方向', null=True, blank=True)

    fromschool = models.CharField(max_length=100, verbose_name='本科大学', null=True, blank=True)
    frommajor = models.CharField(max_length=100, verbose_name='本科专业', null=True, blank=True)

    courses = models.ManyToManyField(Course, null=True, blank=True, verbose_name='课程选择')
    othercourses = models.TextField(verbose_name='其他课程', null=True, blank=True)
    gpa = models.FloatField(verbose_name='本科GPA', null=True, blank=True)
    gpatotal = models.IntegerField(verbose_name='本科GPA满分', null=True, blank=True)
    selfassessment = models.IntegerField(max_length=100, choices=settings.ASSESS_CHOICES, verbose_name='知识掌握程度',
                                         null=True, blank=True)
    poj = models.ManyToManyField(Poj, null=True, blank=True, verbose_name='项目经历')
    otherpoj = models.TextField(verbose_name='其他项目经历', null=True, blank=True)
    goal = models.IntegerField(choices=settings.GOAL_CHOICES, verbose_name='阶段性目标', null=True, blank=True)

    hardship = models.ManyToManyField(Hardship, null=True, blank=True, verbose_name='存在的问题')
    otherhardship = models.TextField(verbose_name='其他问题', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Ques'

    def save(self, *args, **kwargs):
        super().save()
