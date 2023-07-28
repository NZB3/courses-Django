from django.contrib import admin
from .models import Complication


class ComplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Complication, ComplicationAdmin)