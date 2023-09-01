from django.contrib import admin
from .models import Course, FreeTaster

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title'],
    }

admin.site.register(FreeTaster)