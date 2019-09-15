from django.contrib import admin
from .models import TRTLOrder, TRTLOrderAdmin
# Register your models here.
admin.site.register(TRTLOrder,  TRTLOrderAdmin)