from django.contrib import admin

from .models import Offers

class OffersAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_display_links = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')

admin.site.register(Offers, OffersAdmin)