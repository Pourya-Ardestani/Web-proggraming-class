from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from .forms import SignUpStep1Form, SignUpStep2Form
from .models import CustomUser

# Create your views here.

def landing_page_view(request):
    return render(request, 'landing-page.html')


def cart_view(request):
    return render(request, 'cart.html')


def account_info_view(request):
    return render(request, 'account-info.html')


# ... continue for all your .html files ...

def order_history_view(request):
    return render(request, 'Order-history.html')  # Ensure correct capitalization from your filename


def other_products_view(request):
    return render(request, 'other-products.html')


def selected_product_view(request):
    return render(request, 'selected-product.html')



def users_profile_view(request):
    return render(request, 'users-profile.html')

# def user_signup_view(request):
#     return render(request, 'user-signup.html')
#
#
# def user_signup_2_view(request):
#     return render(request, 'user-signup-2.html')


def user_signup_view(request):
    if request.method == 'POST':
        form = SignUpStep1Form(request.POST)
        if form.is_valid():
            user = form.save() # کاربر در دیتابیس ذخیره می شود
            # می توانید user_id را در سشن ذخیره کنید تا در مرحله دوم از آن استفاده کنید
            request.session['user_id_for_signup'] = user.id
            return redirect('user_signup_2') # به صفحه مرحله دوم هدایت می شود
    else:
        initial_data = {
            'full_name': 'نگار زمانی',
            'national_id': '۹۹۹۹۹۹۹۹۹۹',
            'email': 'n.zamani@gmail.com',
            'birthday': '2000-12-12',
        }
        form = SignUpStep1Form(initial=initial_data)
    return render(request, 'user-signup.html', {'form': form})

def user_signup_2_view(request):
    user_id = request.session.get('user_id_for_signup')
    if not user_id:
        return redirect('user_signup') # اگر user_id در سشن نبود، به مرحله اول برگردانید

    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return redirect('user_signup') # اگر کاربر پیدا نشد، به مرحله اول برگردانید

    if request.method == 'POST':
        # instance=user باعث می شود فرم، اطلاعات موجود کاربر را ویرایش کند
        form = SignUpStep2Form(request.POST, instance=user)
        if form.is_valid():
            form.save() # اطلاعات مرحله دوم را ذخیره می کند
            del request.session['user_id_for_signup'] # اطلاعات سشن را پاک کنید
            login(request, user) # کاربر را لاگین کنید
            return redirect('users_profile') # به صفحه داشبورد یا هر صفحه دیگری هدایت کنید
    else:
        # برای نمایش اطلاعات موجود کاربر در فرم مرحله دوم
        initial_data = {
            'mobile_number': '۰۹۱۲۰۰۰۰۰۰۰',
            'phone_number': '۰۲۱۵۵۵۵۵۵۵۵',
            'province': 'تهران',
            'city': 'تهران',
            'address': 'تهران، خیابان ولیعصر، منطقه ۱۲، بلوار کاوه، کوچه ابوذر، پلاک ۱۵',
        }
        form = SignUpStep2Form(instance=user, initial=initial_data)
    return render(request, 'user-signup-2.html', {'form': form, 'user': user})
