from django.contrib import admin
from .models import UserProfile # وارد کردن مدل UserProfile که ساختید

# Register your models here.

admin.site.register(UserProfile)