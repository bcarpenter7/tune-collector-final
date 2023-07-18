from django.contrib import admin
from .models import Tune
# Register your models here.

class TuneAdmin(admin.ModelAdmin):
    list_display = (
        'get_display_name',
        'key',
        'tuning',
        'user',
        'created_at',
        'updated_at',
    )
    search_fields = ('name', 'fiddler', 'description', 'state')
    fieldsets = (
        (None, {'fields': ('name', 'key', 'tuning', 'stars')}),
        ('Optional', {'fields': ('fiddler', 'state', 'description')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
        ('User', {'fields': ('user',)}),
    )
    readonly_fields = ('created_at', 'updated_at')
    add_fieldsets = (
        (None, {'fields': ('name', 'key', 'tuning', 'stars')}),
        ('Optional', {'fields': ('fiddler', 'state', 'description')}),
        ('User', {'fields': ('user',)}),
    )
    ordering = ('-created_at',)

    # make user settable when creating, but not changeable when editing, by checking if obj exists
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields


admin.site.register(Tune, TuneAdmin)
