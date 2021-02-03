from django.contrib import admin
from .models import Course,Event,Registration

# Register your models here.
#
#
#
# class CourseAdmin(admin.ModelAdmin):
#     fields = ['course_name']
#
# class EventAdmin(admin.ModelAdmin):
#     fields = ['event_name']
#
# class RegistrationAdmin(admin.ModelAdmin):
#     fields = [ ]

admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Registration)
