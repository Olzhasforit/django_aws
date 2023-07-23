from django.contrib import admin
from zhas.models import Bucket

class BucketAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'file']


admin.site.register(Bucket, BucketAdmin)

# Register your models here.
