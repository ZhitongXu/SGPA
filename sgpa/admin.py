from django.contrib import admin
from .models import *
import csv
from openpyxl import Workbook
from django.http import HttpResponse
from .models import Course, Poj, Ques, Hardship
from import_export import resources
from import_export.admin import ImportExportModelAdmin


#admin.site.register(Ques)
#admin.site.register(Course)
#admin.site.register(Poj)



class CourseResource(resources.ModelResource):

    class Meta:
        model = Course
        #导出内容
        fields = ('id', 'title')
        #导出顺序
        export_order = ('id', 'title')


class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    # 显示列表展示的字段
    list_display = ['title']
    # 显示搜索项，分开搜索
    list_filter = ('title',)
    # 按照id排序
    ordering = ["-id", ]


admin.site.register(Course, CourseAdmin)


class PojResource(resources.ModelResource):

    class Meta:
        model = Poj
        #导出内容
        fields = ('id', 'title')
        #导出顺序
        export_order = ('id', 'title')


class PojAdmin(ImportExportModelAdmin):
    resource_class = PojResource
    # 显示列表展示的字段
    list_display = ['title']
    # 显示搜索项，分开搜索
    list_filter = ('title',)
    # 按照id排序
    ordering = ["-id", ]


admin.site.register(Poj, PojAdmin)


class HardshipResource(resources.ModelResource):

    class Meta:
        model = Hardship
        #导出内容
        fields = ('id', 'title')
        #导出顺序
        export_order = ('id', 'title')


class HardshipAdmin(ImportExportModelAdmin):
    resource_class = HardshipResource
    # 显示列表展示的字段
    list_display = ['title']
    # 显示搜索项，分开搜索
    list_filter = ('title',)
    # 按照id排序
    ordering = ["-id", ]


admin.site.register(Hardship, HardshipAdmin)



class ExportCsvMixin(object):
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        #field_names = [field.name for field in meta.fields]
        field_names = ['user_id', 'username', 'email', 'courses', 'poj', 'hardship', 'type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'othercourses', 'gpa', 'gpatotal', 'selfassessment', 'otherpoj', 'goal', 'otherhardship']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        response.charset = 'utf-8-sig'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            dat = []
            dat.append(obj.user.pk)
            dat.append(obj.user.username)
            dat.append(obj.user.email)
            dat.append('_'.join([c.title for c in obj.courses.all()]))
            dat.append('_'.join([p.title for p in obj.poj.all()]))
            dat.append('_'.join([h.title for h in obj.hardship.all()]))
            sub_field_names = ['type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'othercourses', 'gpa', 'gpatotal', 'selfassessment', 'otherpoj', 'goal', 'otherhardship']
            rest = [getattr(obj, field) for field in sub_field_names]
            dat.extend(rest)
            row = writer.writerow(dat)
            #row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = '导出CSV'


class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = ['user_id', 'username', 'email', 'courses', 'poj', 'hardship', 'type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'othercourses', 'gpa', 'gpatotal', 'selfassessment', 'otherpoj', 'goal', 'otherhardship']

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            dat = []
            dat.append(obj.user.pk)
            dat.append(obj.user.username)
            dat.append(obj.user.email)
            dat.append('_'.join([c.title for c in obj.courses.all()]))
            dat.append('_'.join([p.title for p in obj.poj.all()]))
            dat.append('_'.join([p.title for p in obj.hardship.all()]))
            sub_field_names = ['type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'othercourses', 'gpa', 'gpatotal', 'selfassessment',
                               'otherpoj', 'goal', 'otherhardship']
            rest = [getattr(obj, field) for field in sub_field_names]
            dat.extend(rest)
            row = ws.append(dat)

        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'


class QuesAdmin(admin.ModelAdmin, ExportCsvMixin, ExportExcelMixin):
    fields = ('user_id', 'username', 'email', 'type', 'enteryear', 'fromschool', 'frommajor', 'teafield',
              'courses', 'othercourses', 'gpa', 'gpatotal', 'selfassessment',
              'poj', 'otherpoj', 'goal', 'hardship', 'otherhardship')
    readonly_fields = ('user_id', 'username', 'email')
    list_display = ('user_id', 'username', 'email', 'type', 'enteryear', 'fromschool', 'frommajor', 'teafield', 'goal')
    list_filter = ('type', 'teafield', 'goal')
    actions = ['export_as_csv', 'export_as_excel']

    def user_id(self, obj):
        return obj.user.pk

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def 课程选择(self, obj):
        return [c.title for c in obj.courses.all()]

    def 项目经历(self, obj):
        return [p.title for p in obj.poj.all()]

    def 存在的问题(self, obj):
        return [h.title for h in obj.hardship.all()]


admin.site.register(Ques, QuesAdmin)
