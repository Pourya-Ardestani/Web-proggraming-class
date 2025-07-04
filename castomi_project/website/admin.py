from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # برای سفارشی سازی پنل ادمین کاربر
from .models import CustomUser

# Register your models here.
# این کلاس به شما امکان می دهد فیلدهای CustomUser را در پنل ادمین مدیریت کنید
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # فیلدهایی که در لیست کاربران در پنل ادمین نمایش داده می شوند
    list_display = ('username', 'email', 'full_name', 'national_id', 'is_staff', 'mobile_number', 'phone_number')

    # فیلدهایی که در صفحه ویرایش کاربر نمایش داده می شوند
    # UserAdmin.fieldsets شامل فیلدهای پیش فرض (username, password, permissions, etc.) است
    fieldsets = UserAdmin.fieldsets + (
        (('اطلاعات تکمیلی'), {'fields': ('full_name', 'national_id', 'education', 'job', 'birthday', 'mobile_number', 'phone_number', 'province', 'city', 'address', 'postal_code')}),
    )

    # اگر می خواهید فیلدهای جدید در بخش "Add user" (افزودن کاربر جدید) هم نمایش داده شوند
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('اطلاعات تکمیلی'), {'fields': ('full_name', 'national_id', 'education', 'job', 'birthday', 'mobile_number', 'phone_number', 'province', 'city', 'address', 'postal_code')}),
    )
