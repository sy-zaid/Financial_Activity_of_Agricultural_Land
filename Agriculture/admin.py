from django.contrib import admin
from Agriculture.models import Machinery,Seeds,Crops, Purchase_Crops,Loan

# Register your models here.
admin.site.register(Machinery)
admin.site.register(Seeds)
admin.site.register(Crops)
admin.site.register(Purchase_Crops)
admin.site.register(Loan)