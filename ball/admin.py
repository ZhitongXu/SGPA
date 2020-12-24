from import_export import resources
from .models import Keyword
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class KeywordResource(resources.ModelResource):

    class Meta:
        model = Keyword
        #导出内容
        fields = ('id', 'title', 'type')
        #导出顺序
        export_order = ('id', 'title', 'type')


class KeywordAdmin(ImportExportModelAdmin):
    resource_class = KeywordResource
    # 显示列表展示的字段
    list_display = ['title', 'type']
    # 显示搜索项，分开搜索
    list_filter = ('title', 'type')
    # 按照id排序
    ordering = ["-id", ]


admin.site.register(Keyword, KeywordAdmin)
