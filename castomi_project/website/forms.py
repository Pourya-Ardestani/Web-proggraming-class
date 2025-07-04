from django import forms
from .models import CustomUser

class SignUpStep1Form(forms.ModelForm):
    # فیلدهای مرحله اول
    # email و password از AbstractUser به صورت خودکار مدیریت می شوند
    # اگر می خواهید password را دوباره تایید کنید، باید یک فیلد جداگانه برای تایید رمز عبور اضافه کنید.
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field left-align'}), label="کلمه عبور")
    
    class Meta:
        model = CustomUser
        fields = [
            'full_name',
            'national_id',
            'education',
            'job',
            'email',
            'password',
            'birthday'
        ]
        # اگر نمی خواهید username را از کاربر بگیرید و می خواهید از email به عنوان username استفاده کنید،
        # می توانید username را exclude کنید و در view آن را برابر با email قرار دهید.
        # exclude = ['username']

        widgets = {
                'full_name': forms.TextInput(attrs={'class': 'input-field'}),
                'national_id': forms.TextInput(attrs={'class': 'input-field left-align'}),
                'education': forms.Select(attrs={'class': 'input-field'}), # مطمئن شوید که اینجا forms.Select هست
                'job': forms.Select(attrs={'class': 'input-field'}),
                'email': forms.EmailInput(attrs={'class': 'input-field left-align'}),
                'birthday': forms.DateInput(attrs={'class': 'input-field left-align', 'type': 'date'}), # برای type="date"
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # فقط در صورتی که فرم جدیدی ایجاد می شود (نه برای ویرایش یک آبجکت موجود)
        if not self.instance.pk:  # اگر آبجکت CustomUser هنوز ذخیره نشده باشد (جدید باشد)
            self.fields['full_name'].initial = 'نگار زمانی'
            self.fields['national_id'].initial = '۹۹۹۹۹۹۹۹۹۹'  # کد ملی ۱۰ رقمی است
            self.fields['email'].initial = 'n.zamani@gmail.com'
            self.fields['password'].initial = '۹۹۹۹۹۹۹'  # توجه: این فقط برای نمایش است، پسورد باید هش شود
            self.fields['birthday'].initial = '2000-12-12'  # فرمت تاریخ باید YYYY-MM-DD باشد
            self.fields['education'].empty_label = "انتخاب کنید"
            self.fields['job'].empty_label = "انتخاب کنید"
            # برای education و job اگر مقادیر پیش‌فرض خاصی دارید
            # self.fields['education'].initial = 'دیپلم'
            # self.fields['job'].initial = 'دانشجو'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت نام کرده است.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.username = self.cleaned_data["email"]  # این خط را اضافه کنید

        if commit:
            user.save()
        return user


class SignUpStep2Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'mobile_number',
            'phone_number',
            'province',
            'city',
            'address'
        ]
        # email در این مرحله فقط برای نمایش است و تغییر نمی کند
        # اگر می خواهید email را در این مرحله هم قابل ویرایش کنید، آن را در fields اضافه کنید.
        # اگر نمی خواهید نمایش داده شود، اینجا نباشد.
        # fields = ['mobile_number', 'phone_number', 'province', 'city', 'address', 'email']
        widgets = {
        'mobile_number': forms.TextInput(attrs={'class': 'input-field left-align'}),
        'phone_number': forms.TextInput(attrs={'class': 'input-field left-align'}),
        'province': forms.Select(attrs={'class': 'input-field'}),
        'city': forms.Select(attrs={'class': 'input-field'}),
        'address': forms.Textarea(attrs={'class': 'input-field'}), # برای Textarea
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # این بخش برای مرحله دوم کمتر کاربرد دارد چون instance از قبل وجود دارد
            self.fields['mobile_number'].initial = '۰۹۱۲۰۰۰۰۰۰۰'
            self.fields['phone_number'].initial = '۰۲۱۵۵۵۵۵۵۵۵'
            self.fields['province'].initial = 'تهران'
            self.fields['city'].initial = 'تهران'
            self.fields['address'].initial = 'تهران، خیابان ولیعصر، منطقه ۱۲، بلوار کاوه، کوچه ابوذر، پلاک ۱۵'
