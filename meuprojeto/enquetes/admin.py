from django.contrib import admin
from .models import Enquete


@admin.register(Enquete)
class EnqueteAdmin(admin.ModelAdmin):
    readonly_fields = ('data_publicacao', )
    list_display = ['texto', 'data_publicacao']
    list_filter = ['data_publicacao']
    search_fields = ['texto']
