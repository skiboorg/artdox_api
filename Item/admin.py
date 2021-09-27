from django_summernote.admin import SummernoteModelAdmin
from .models import Item
from django.contrib import admin

class ItemAdmin(SummernoteModelAdmin):
    pass
    # summernote_fields = ('description',)

admin.site.register(Item)