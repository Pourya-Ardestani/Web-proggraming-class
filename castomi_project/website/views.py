from django.shortcuts import render


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


def user_signup_view(request):
    return render(request, 'user-signup.html')


def user_signup_2_view(request):
    return render(request, 'user-signup-2.html')


def users_profile_view(request):
    return render(request, 'users-profile.html')
