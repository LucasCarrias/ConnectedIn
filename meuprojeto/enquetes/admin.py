from django.contrib import admin
from .models import Enquete
# Register your models here.
class EnqueteAdmin(admin.ModelAdmin):
    readonly_fields = ('data_publicacao', )

admin.site.register(Enquete, EnqueteAdmin)