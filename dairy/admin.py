from django.contrib import admin
from dairy.models import Dairy

class DairyAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Dairy, DairyAdmin)

