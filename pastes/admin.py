from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Paste

@admin.register(Paste)
class ViewAdmin(ImportExportModelAdmin):
    pass