from django.contrib import admin
from .models import Report
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class ReportResource(resources.ModelResource):
    class Meta:
        model = Report
        # skip_unchanged = True
        # fields = '__all__'

@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
#    pass
    list_display = ('published_date','report_title', 'main_category', 'pages', 'companies_mentioned', 'single_user_licence', 'multi_user_licence', 'corporate_user_licence')

# class ReportAdmin(ImportExportModelAdmin):
#     resource_class = ReportResource

# admin.site.register(Report, ReportAdmin)
