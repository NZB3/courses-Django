from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'assessment')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')


admin.site.register(Review, ReviewAdmin)
