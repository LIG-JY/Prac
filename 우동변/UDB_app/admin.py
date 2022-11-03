from django.contrib import admin
from .models import CommissionedArea
from Database.lawyer_dao import ca_collection

admin.site.register(CommissionedArea)
# admin.site.register(ca_collection)

# Register your models here.
