from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(WithdrawalRequest)
admin.site.register(PaymentType)
