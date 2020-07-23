from django.contrib import admin
from .models import inputClient, MbtiResult

# Register your models here.
admin.site.register(MbtiResult)
# admin.site.register(lawywerAccount)
admin.site.register(inputClient)