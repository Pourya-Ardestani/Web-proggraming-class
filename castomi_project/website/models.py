from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission # Import all necessary classes

# Create your models here.

class CustomUser(AbstractUser):
    # فیلدهای مرحله اول ثبت نام
    full_name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    national_id = models.CharField(max_length=10, unique=True, verbose_name="کد ملی") # کد ملی معمولا unique است

    # تعریف گزینه‌های تحصیلات
    EDUCATION_CHOICES = [
        ('diploma', 'دیپلم'),
        ('associate', 'فوق دیپلم'),
        ('bachelor', 'کارشناسی'),
        ('master', 'کارشناسی ارشد'),
        ('phd', 'دکترا'),
        ('other', 'سایر'),
    ]
    # فیلد education فقط یک بار تعریف می‌شود
    education = models.CharField(
        max_length=100,
        choices=EDUCATION_CHOICES,
        blank=True,
        null=True,
        verbose_name="تحصیلات"
    )

    # تعریف گزینه‌های شغل
    JOB_CHOICES = [
        ('student', 'دانشجو'),
        ('employee', 'کارمند'),
        ('self_employed', 'صاحب کسب و کار/آزاد'),
        ('unemployed', 'بیکار'),
        ('retired', 'بازنشسته'),
        ('other', 'سایر'),
    ]
    job = models.CharField(
        max_length=100,
        choices=JOB_CHOICES,
        blank=True,
        null=True,
        verbose_name="شغل"
    )

    PROVINCE_CHOICES = [
        ('', 'انتخاب کنید'), # گزینه پیش فرض خالی
        ('tehran', 'تهران'),
        ('isfahan', 'اصفهان'),
        ('fars', 'فارس'),
        ('khorasan_razavi', 'خراسان رضوی'),
        ('alborz', 'البرز'),
        # ... می توانید استان های بیشتری اضافه کنید
    ]
    province = models.CharField(
        max_length=100,
        choices=PROVINCE_CHOICES,
        blank=True,
        null=True,
        verbose_name="استان"
    )

    # تعریف گزینه‌های شهر (این لیست معمولا خیلی بزرگ است و بهتر است داینامیک باشد)
    CITY_CHOICES = [
        ('', 'انتخاب کنید'), # گزینه پیش فرض خالی
        ('tehran_city', 'تهران'),
        ('karaj', 'کرج'),
        ('mashhad', 'مشهد'),
        ('isfahan_city', 'اصفهان'),
        ('shiraz', 'شیراز'),
        # ... می توانید شهرهای بیشتری اضافه کنید
    ]
    city = models.CharField(
        max_length=100,
        choices=CITY_CHOICES,
        blank=True,
        null=True,
        verbose_name="شهر"
    )
    # فیلد job فقط یک بار تعریف می‌شود

    # email و password در AbstractUser وجود دارند و نیازی به تعریف مجدد نیست
    birthday = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")

    # فیلدهای مرحله دوم ثبت نام
    mobile_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره موبایل")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره تلفن")
    # province = models.CharField(max_length=100, blank=True, null=True, verbose_name="استان")
    # city = models.CharField(max_length=100, blank=True, null=True, verbose_name="شهر")
    address = models.TextField(blank=True, null=True, verbose_name="آدرس کامل پستی")
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="آدرس ایمیل")
    postal_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="کد پستی")

    # USERNAME_FIELD = 'email' # حالا کاربر با ایمیل لاگین می کند
    # REQUIRED_FIELDS = ['full_name', 'national_id'] # فیلدهایی که هنگام createsuperuser اجباری هستند (username دیگر اجباری نیست)


    # می‌توانید یک فیلد برای پیگیری مرحله ثبت نام اضافه کنید (اختیاری)
    # registration_step = models.IntegerField(default=1)

    # این بخش‌ها برای رفع خطاهای E336 و E300 حیاتی هستند
    # related_name ها باید منحصر به فرد باشند
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_groups_set", # نام منحصر به فرد برای related_name
        related_query_name="customuser_group",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customuser_permissions_set", # نام منحصر به فرد برای related_name
        related_query_name="customuser_permission",
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.email # یا self.username یا self.full_name
