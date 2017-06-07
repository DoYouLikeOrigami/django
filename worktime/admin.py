from django.contrib import admin

from .models import Driver

# Register your models here.

class DriverModelAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'driverclass', 'status']
	list_display_links = ['__str__', 'status']
	list_filter = ['driverclass', 'status']
	search_fields = ['passport']
	#list_editable = ['passport']

	class Meta:
		model = Driver
		

admin.site.register(Driver, DriverModelAdmin)