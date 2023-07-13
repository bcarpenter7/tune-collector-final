from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from account.models import MyUser


class MyUserAdmin(UserAdmin):
	list_display = ('username', 'email', 'created_at', 'updated_at', 'last_login', 'is_staff', 'is_superuser', 'is_active')
	search_fields = ('username', 'email')
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
		('Timestamps', {'fields': ('created_at', 'updated_at', 'last_login')}),
	)
	readonly_fields = ('created_at', 'updated_at', 'last_login')
	add_fieldsets = ((None, {'fields': ('username', 'email', 'password1', 'password2')}), ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}))
	ordering = ('username',)


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)
