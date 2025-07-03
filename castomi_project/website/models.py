from django.db import models

# Create your models here.
# website/models.py
from django.db import models
from django.contrib.auth.models import User

# تعریف گزینه‌ها برای فیلدهای انتخابی (مثل تحصیلات و شغل)
# اینها رو اینجا تعریف می‌کنیم تا هم در مدل و هم در فرم‌ها بتونیم ازشون استفاده کنیم
EDUCATION_CHOICES = [
    ('diploma', 'دیپلم'),
    ('associate', 'فوق دیپلم'),
    ('bachelor', 'کارشناسی'),
    ('master', 'کارشناسی ارشد'),
    ('phd', 'دکترا'),
    ('other', 'سایر'),
]

JOB_CHOICES = [
    ('student', 'دانشجو'),
    ('employee', 'کارمند'),
    ('freelancer', 'فریلنسر'),
    ('unemployed', 'بیکار'),
    ('other', 'سایر'),
]

class UserProfile(models.Model):
    # این فیلد، مدل UserProfile رو به یک کاربر خاص در سیستم احراز هویت جنگو متصل می‌کنه.
    # هر کاربر (User) فقط یک پروفایل (UserProfile) می‌تونه داشته باشه (OneToOneField).
    # وقتی کاربر حذف میشه، پروفایلش هم حذف میشه (on_delete=models.CASCADE).
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # ----------------------------------------------------
    # فیلدهایی که از فرم اول (user-signup.html) میان:
    # ----------------------------------------------------
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="نام و نام خانوادگی")
    # 'blank=True' یعنی این فیلد در فرم می‌تونه خالی فرستاده بشه.
    # 'null=True' یعنی این فیلد در دیتابیس می‌تونه NULL باشه.
    # 'verbose_name' همون نامی هست که در پنل ادمین یا خطاهای جنگو نمایش داده میشه.

    national_code = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name="کد ملی")
    # 'unique=True' تضمین می‌کنه که کد ملی برای هر کاربر منحصر به فرد باشه.

    education = models.CharField(max_length=50, choices=EDUCATION_CHOICES, blank=True, null=True, verbose_name="تحصیلات")
    # 'choices' باعث میشه که این فیلد در فرم به صورت Dropdown (select) نمایش داده بشه.

    job = models.CharField(max_length=50, choices=JOB_CHOICES, blank=True, null=True, verbose_name="شغل")

    birthday = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")
    # 'DateField' برای ذخیره تاریخ مناسبه.

    # ----------------------------------------------------
    # فیلدهایی که از فرم دوم (user-signup-2.html) میان:
    # ----------------------------------------------------
    mobile_number = models.CharField(max_length=15, blank=True, null=True, unique=True, verbose_name="شماره موبایل")
    # 'unique=True' برای شماره موبایل هم خوبه.

    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره تلفن ثابت")

    province = models.CharField(max_length=100, blank=True, null=True, verbose_name="استان")

    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="شهر")

    address = models.TextField(blank=True, null=True, verbose_name="آدرس کامل پستی")
    # 'TextField' برای آدرس‌های طولانی مناسبه.

    # ----------------------------------------------------
    # متد __str__ برای نمایش بهتر آبجکت در پنل ادمین
    # ----------------------------------------------------
    def __str__(self):
        return f"پروفایل {self.user.username}"