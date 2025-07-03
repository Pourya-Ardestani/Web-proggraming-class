from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('cart/', views.cart_view, name='cart'),
    path('account-info/', views.account_info_view, name='account_info'),
    path('order-history/', views.order_history_view, name='order_history'),
    path('other-products/', views.other_products_view, name='other_products'),
    path('selected-product/', views.selected_product_view, name='selected_product'),
    # path('signup/', views.user_signup_view, name='user_signup'),
    # path('signup-2/', views.user_signup_2_view, name='user_signup_2'),
    path('profile/', views.users_profile_view, name='users_profile'),
    ###---

    # مسیر برای ثبت‌نام کاربر
    #  path('register/', views.register_request, name='register'),
    # path('signup-info/', views.signup_profile_info_view, name='signup_profile_info'),
    path('signup/', views.register_request, name='user_signup'),
     path('signup-2/', views.signup_profile_info_view, name='user_signup_2'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    

]