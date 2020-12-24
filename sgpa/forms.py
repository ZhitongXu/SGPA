from django import forms
from .models import Course, Poj, Ques, Hardship
from django.conf import settings
from django.forms.widgets import SelectDateWidget


class QuesForm(forms.ModelForm):
    type = forms.ChoiceField(label='入学类型',
                             choices=settings.TYPE_CHOICES,
                             widget=forms.RadioSelect(),
                             required=True)
    enteryear = forms.IntegerField(label='入学年份', required=True)
    teafield = forms.ChoiceField(label='导师方向',
                                 choices=settings.FIELD_CHOICES,
                                 widget=forms.RadioSelect(),
                                 required=True)
    fromschool = forms.CharField(label='本科大学', required=True)
    frommajor = forms.CharField(label='本科专业', required=True)
    courses = forms.ModelMultipleChoiceField(label='本科曾经上过的课程，包括：',
                                             queryset=Course.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=True)
    gpa = forms.FloatField(label='本科GPA', required=True)
    gpatotal = forms.IntegerField(label='本科GPA满分', required=True)
    selfassessment = forms.ChoiceField(label='本科统计专业知识掌握程度自我评价',
                                       choices=settings.ASSESS_CHOICES,
                                       widget=forms.RadioSelect(),
                                       required=True)
    poj = forms.ModelMultipleChoiceField(label='项目经历',
                                         queryset=Poj.objects.all(),
                                         widget=forms.CheckboxSelectMultiple(),
                                         required=True)
    goal = forms.ChoiceField(label='研究生期间的阶段性目标',
                             choices=settings.GOAL_CHOICES,
                             widget=forms.RadioSelect(),
                             required=True)
    hardship = forms.ModelMultipleChoiceField(label='存在的问题，包括：',
                                              queryset=Hardship.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(),
                                              required=True)

    class Meta:
        model = Ques
        fields = ['type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'courses', 'othercourses',
                  'gpa', 'gpatotal', 'selfassessment', 'poj', 'otherpoj', 'goal', 'hardship', 'otherhardship']


class QuesUpdateForm(forms.ModelForm):
    type = forms.ChoiceField(label='入学类型',
                             choices=settings.TYPE_CHOICES,
                             widget=forms.RadioSelect(),
                             required=True)
    enteryear = forms.IntegerField(label='入学年份', required=True)
    teafield = forms.ChoiceField(label='导师方向',
                                 choices=settings.FIELD_CHOICES,
                                 widget=forms.RadioSelect(),
                                 required=True)
    fromschool = forms.CharField(label='本科大学', required=True)
    frommajor = forms.CharField(label='本科专业', required=True)
    courses = forms.ModelMultipleChoiceField(label='本科曾经上过的课程，包括：',
                                             queryset=Course.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=True)
    gpa = forms.FloatField(label='本科GPA', required=True)
    gpatotal = forms.IntegerField(label='本科GPA满分', required=True)
    selfassessment = forms.ChoiceField(label='本科统计专业知识掌握程度自我评价',
                                       choices=settings.ASSESS_CHOICES,
                                       widget=forms.RadioSelect(),
                                       required=True)
    poj = forms.ModelMultipleChoiceField(label='项目经历',
                                         queryset=Poj.objects.all(),
                                         widget=forms.CheckboxSelectMultiple(),
                                         required=True)
    goal = forms.ChoiceField(label='研究生期间的阶段性目标',
                             choices=settings.GOAL_CHOICES,
                             widget=forms.RadioSelect(),
                             required=True)
    hardship = forms.ModelMultipleChoiceField(label='存在的问题，包括：',
                                              queryset=Hardship.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(),
                                              required=True)


    class Meta:
        model = Ques
        fields = ['type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'courses', 'othercourses',
                  'gpa', 'gpatotal', 'selfassessment', 'poj', 'otherpoj', 'goal', 'hardship', 'otherhardship']
