from django.contrib import admin
from .models import PaintList, Paint
# Register your models here.


class PaintListAdmin(admin.ModelAdmin):
    pass


admin.site.register(PaintList, PaintListAdmin)
admin.site.register(Paint, PaintListAdmin)
