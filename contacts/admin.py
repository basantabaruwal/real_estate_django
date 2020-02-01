from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('listing', 'name', 'email', 'phone', 'contact_date',)
    list_display_links = ('listing', 'name',)
    list_filter = ('listing', 'name','contact_date',)
    search_fields = ('listing', 'name', 'contact_date',)
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
