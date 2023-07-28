from django.contrib import admin
from .models import Direction


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Direction, DirectionAdmin)