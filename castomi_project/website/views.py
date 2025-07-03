from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout # توابع اصلی احراز هویت جنگو
from django.contrib import messages # برای نمایش پیام‌ها (مثل موفقیت یا خطا)
from django.contrib.auth.decorators import login_required # برای محافظت از Viewها

# فرم‌هایی که در website/forms.py تعریف کردیم
from .forms import CustomUserCreationForm, UserProfileInfoForm, CustomAuthenticationForm

# مدلی که در website/models.py تعریف کردیم
from .models import UserProfile


# Create your views here.

def landing_page_view(request):
    return render(request, 'landing-page.html')


def cart_view(request):
    return render(request, 'cart.html')


def account_info_view(request):
    return render(request, 'account-info.html')


def order_history_view(request):
    return render(request, 'Order-history.html')  # Ensure correct capitalization from your filename


def other_products_view(request):
    return render(request, 'other-products.html')


def selected_product_view(request):
    return render(request, 'selected-product.html')


def user_signup_view(request):
    return render(request, 'user-signup.html')


def user_signup_2_view(request):
    return render(request, 'user-signup-2.html')


def users_profile_view(request):
    return render(request, 'users-profile.html')


####################################
####################################section 2


# ----------------------------------------------------
# View برای صفحه ثبت‌نام (user-signup.html)
# این View فرم CustomUserCreationForm را پردازش می‌کند.
# ----------------------------------------------------
def register_request(request):
    if request.method == "POST":
        # فرم را با اطلاعات POST پر می‌کنیم
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # اگر فرم معتبر بود، متد save() در CustomUserCreationForm فراخوانی می‌شود
            # و هم کاربر اصلی (User) و هم پروفایل اولیه (UserProfile) را ذخیره می‌کند.
            user = form.save()
            login(request, user) # کاربر بلافاصله بعد از ثبت‌نام وارد می‌شود
            messages.success(request, "ثبت نام شما با موفقیت انجام شد و وارد شدید.")
            # کاربر را به صفحه اطلاعات تکمیلی پروفایل هدایت می‌کنیم
            return redirect("user_signup_2")
        else:
            # اگر فرم نامعتبر بود، پیام‌های خطا را جمع‌آوری و نمایش می‌دهیم
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"خطا در فیلد {form.fields[field].label}: {error}")
    else:
        # اگر درخواست GET بود (اولین بار که صفحه باز می‌شود)، یک فرم خالی نمایش می‌دهیم
        form = CustomUserCreationForm()

    # رندر کردن تمپلیت user-signup.html با آبجکت فرم
    return render(request, "user-signup.html", {"form": form})

# ----------------------------------------------------
# View برای صفحه ورود (Login)
# این View فرم CustomAuthenticationForm را پردازش می‌کند.
# ----------------------------------------------------
def login_request(request):
    if request.method == "POST":
        # فرم ورود را با درخواست و داده‌های POST پر می‌کنیم
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # اعتبار سنجی کاربر با نام کاربری و رمز عبور
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) # کاربر را وارد سیستم می‌کنیم
                messages.info(request, f"خوش آمدید، {username}!")
                # هدایت به صفحه اصلی یا داشبورد بعد از ورود موفق
                return redirect("landing_page")
            else:
                messages.error(request, "نام کاربری یا رمز عبور نامعتبر است.")
        else:
            messages.error(request, "نام کاربری یا رمز عبور نامعتبر است.")
    else:
        # اگر درخواست GET بود، یک فرم خالی نمایش می‌دهیم
        form = CustomAuthenticationForm()

    # رندر کردن تمپلیت user-signup.html (یا یک تمپلیت جداگانه برای لاگین) با آبجکت فرم
    return render(request, "user-signup.html", {"form": form})

# ----------------------------------------------------
# View برای صفحه خروج (Logout)
# ----------------------------------------------------
def logout_request(request):
    logout(request) # کاربر را از سشن خارج می‌کند
    messages.info(request, "شما با موفقیت از حساب کاربری خود خارج شدید.")
    # هدایت به صفحه اصلی یا هر صفحه دلخواه بعد از خروج
    return redirect("landing_page")

# ----------------------------------------------------
# View برای صفحه اطلاعات تکمیلی پروفایل (user-signup-2.html)
# این View فرم UserProfileInfoForm را پردازش می‌کند.
# فقط کاربران وارد شده می‌توانند به این صفحه دسترسی داشته باشند (@login_required)
# ----------------------------------------------------
@login_required
def signup_profile_info_view(request):
    # پیدا کردن یا ایجاد پروفایل کاربر فعلی (اگر وجود نداشت، ایجاد می‌شود)
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # فرم را با اطلاعات POST و نمونه موجود پروفایل پر می‌کنیم
        form = UserProfileInfoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save() # اطلاعات پروفایل در دیتابیس ذخیره/به‌روزرسانی می‌شود
            messages.success(request, "اطلاعات تکمیلی پروفایل با موفقیت ذخیره شد.")
            # هدایت به صفحه اصلی پروفایل کاربر بعد از ذخیره
            return redirect("users_profile")
        else:
            # نمایش خطاهای فرم
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"خطا در فیلد {form.fields[field].label}: {error}")
    else:
        # اگر درخواست GET بود، فرم را با اطلاعات موجود پروفایل پر می‌کنیم
        form = UserProfileInfoForm(instance=user_profile)

    # context برای ارسال اطلاعات به تمپلیت
    context = {
        'form': form,
        'user_email': request.user.email, # ایمیل کاربر جنگو (از مدل User)
    }
    # رندر کردن تمپلیت user-signup-2.html با آبجکت فرم و context
    return render(request, "user-signup-2.html", context)

# ----------------------------------------------------
# View برای صفحه پروفایل کاربر (users-profile.html)
# این View فقط اطلاعات کاربر را نمایش می‌دهد.
# ----------------------------------------------------
@login_required # فقط کاربران وارد شده می‌توانند به این صفحه دسترسی داشته باشند
def users_profile_view(request):
    # کاربر فعلی
    current_user = request.user
    # پیدا کردن پروفایل مربوط به کاربر فعلی (یا ایجاد آن در صورت عدم وجود)
    user_profile, created = UserProfile.objects.get_or_create(user=current_user)

    context = {
        'user': current_user,       # آبجکت User جنگو (شامل username, email, first_name, last_name)
        'user_profile': user_profile, # آبجکت UserProfile (شامل اطلاعات اضافی مثل شماره موبایل، آدرس و...)
    }
    # رندر کردن تمپلیت users-profile.html با اطلاعات کاربر و پروفایلش
    return render(request, "users-profile.html", context)


# ----------------------------------------------------
# View برای صفحه Account Info (account-info.html)
# این View فرم UserProfileInfoForm را برای ویرایش اطلاعات پروفایل پردازش می‌کند.
# ----------------------------------------------------
@login_required
def account_info_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # فرم را با اطلاعات POST و نمونه موجود پروفایل پر می‌کنیم
        form = UserProfileInfoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save() # اطلاعات پروفایل در دیتابیس ذخیره/به‌روزرسانی می‌شود
            messages.success(request, "اطلاعات حساب با موفقیت به روز شد.")
            # هدایت به صفحه پروفایل کاربر بعد از ذخیره
            return redirect('users_profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"خطا در فیلد {form.fields[field].label}: {error}")
    else:
        # اگر درخواست GET بود، فرم را با اطلاعات موجود پروفایل پر می‌کنیم
        form = UserProfileInfoForm(instance=user_profile)

    context = {
        'form': form,
        'user_email': request.user.email, # ایمیل کاربر جنگو (برای نمایش در صفحه)
    }
    return render(request, "account-info.html", context)

