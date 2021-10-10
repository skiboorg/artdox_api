from django_summernote.admin import SummernoteModelAdmin
from .models import *
from django.contrib import admin

class ItemAdmin(SummernoteModelAdmin):
    pass
    # summernote_fields = ('description',)

admin.site.register(Item)
admin.site.register(Collection)
admin.site.register(ItemStatus)