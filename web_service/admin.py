from django.contrib import admin
from web_service.forms import WebService_AdminForm
from web_service.models import Web_Service, Web_Service_Level

class Web_Service_Admin(admin.ModelAdmin):
	list_display = ('name', 'location', 'level', 'actual_url', 'alias_url', 'mxd', 'web_adapter')
	search_fields = ('name',)
	form = WebService_AdminForm

admin.site.register(Web_Service, Web_Service_Admin)
admin.site.register(Web_Service_Level)