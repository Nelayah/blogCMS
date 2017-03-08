from django.contrib import admin
from others.models import Others

class OthersAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Others, OthersAdmin)

