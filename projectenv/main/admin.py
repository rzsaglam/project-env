from django.contrib import admin
from .models import Paint
# Register your models here.


class PaintListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paint, PaintListAdmin)
