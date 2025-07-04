from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # برای سفارشی سازی پنل ادمین کاربر
from .models import CustomUser

# Register your models here.
# این کلاس به شما امکان می دهد فیلدهای CustomUser را در پنل ادمین مدیریت کنید
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'national_id', 'is_staff',  'mobile_number', 'phone_number')
