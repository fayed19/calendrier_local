from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_time', 'end_time', 'category')
    search_fields = ('title', 'location', 'category')
    list_filter = ('category', 'start_time')