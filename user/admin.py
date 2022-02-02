from django.contrib import admin
from .models import *
class ContactFormInline (admin.TabularInline):
    model = ContactForm
    extra = 0

class WithdrawalRequestInline (admin.TabularInline):
    model = WithdrawalRequest
    extra = 0

class ReturnFormInline (admin.TabularInline):
    model = ReturnForm
    extra = 0

class StoreFormInline (admin.TabularInline):
    model = StoreForm
    extra = 0

class TransactionInline (admin.TabularInline):
    model = Transaction
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [ContactFormInline,ReturnFormInline,StoreFormInline,TransactionInline,WithdrawalRequestInline]
    search_fields = ('email', 'id', )

admin.site.register(User,UserAdmin)
admin.site.register(WithdrawalRequest)
admin.site.register(PaymentType)
admin.site.register(ContactForm)
admin.site.register(ReturnForm)
admin.site.register(StoreForm)