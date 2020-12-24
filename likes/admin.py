from django.contrib import admin
from .models import *
import csv
from openpyxl import Workbook
from django.http import HttpResponse
from .models import LikeRecord


class ExportCsvMixin(object):
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        #field_names = [field.name for field in meta.fields]
        field_names = ['user_id', 'object_id']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        response.charset = 'utf-8-sig'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            dat = []
            dat.append(obj.user.pk)
            sub_field_names = ['object_id']
            rest = [getattr(obj, field) for field in sub_field_names]
            dat.extend(rest)
            row = writer.writerow(dat)
            #row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = '导出CSV'


class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = ['user_id', 'object_id']

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            dat = []
            dat.append(obj.user.pk)
            sub_field_names = ['object_id']
            rest = [getattr(obj, field) for field in sub_field_names]
            dat.extend(rest)
            row = ws.append(dat)

        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'


class LikeRecordAdmin(admin.ModelAdmin, ExportCsvMixin, ExportExcelMixin):
    fields = ('user_id', 'object_id')
    readonly_fields = ('user_id',)
    list_display = ('user_id', 'object_id')
    list_filter = ('user_id', 'object_id')
    actions = ['export_as_csv', 'export_as_excel']

    def user_id(self, obj):
        return obj.user.pk


admin.site.register(LikeRecord, LikeRecordAdmin)
