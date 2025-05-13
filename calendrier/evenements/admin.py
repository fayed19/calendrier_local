from django.contrib import admin
from .models import Event, Location, Organizer, Category

# Register your models here.

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('title', 'location', 'start_time', 'end_time', 'category')
#     search_fields = ('title', 'location', 'category')
#     list_filter = ('category', 'start_time')


admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Organizer)
admin.site.register(Category)