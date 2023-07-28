from django.contrib import admin
from .models import Profession


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'direction', )
    list_display_links = ('title',)
    search_fields = ('title', )


admin.site.register(Profession, ProfessionAdmin)
