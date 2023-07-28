from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'creator', )
    list_display_links = ('title', )
    search_fields = ('title', 'description')


admin.site.register(Course, CourseAdmin)
