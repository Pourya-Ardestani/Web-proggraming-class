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
            'postal_code',
            'address'
        ]
        widgets = {
        'mobile_number': forms.TextInput(attrs={'class': 'input-field left-align'}),
        'phone_number': forms.TextInput(attrs={'class': 'input-field left-align'}),
        'province': forms.Select(attrs={'class': 'input-field'}),
        'city': forms.Select(attrs={'class': 'input-field'}),
        'postal_code': forms.TextInput(attrs={'class': 'input-field left-align'}),
        'address': forms.Textarea(attrs={'class': 'input-field'}), # برای Textarea
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # این بخش برای مرحله دوم کمتر کاربرد دارد چون instance از قبل وجود دارد
            self.fields['mobile_number'].initial = '۰۹۱۲۰۰۰۰۰۰۰'
            self.fields['phone_number'].initial = '۰۲۱۵۵۵۵۵۵۵۵'
            self.fields['province'].initial = 'تهران'
            self.fields['city'].initial = 'تهران'
            self.fields['postal_code'].initial = '423842-04234'
            self.fields['address'].initial = 'تهران، خیابان ولیعصر، منطقه ۱۲، بلوار کاوه، کوچه ابوذر، پلاک ۱۵'


################
################# adding for section 4


# فرم برای ویرایش اطلاعات حساب کاربری
class AccountInfoForm(forms.ModelForm):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور جدید خود را وارد کنید', 'class': 'form-control'}),
        label="کلمه عبور جدید",
        required=False
    )
    new_password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور جدید خود را مجددا وارد کنید', 'class': 'form-control'}),
        label="تکرار کلمه عبور جدید",
        required=False
    )

    class Meta:
        model = CustomUser
        fields = [
            'full_name',
            'national_id',
            'education',
            'job',
            'birthday',
            'email',
            'mobile_number',
            'phone_number',
            'province',
            'city',
            'address',
            'postal_code',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'select-wrapper'}),
            'job': forms.Select(attrs={'class': 'select-wrapper'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.Select(attrs={'class': 'select-wrapper'}),
            'city': forms.Select(attrs={'class': 'select-wrapper'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['education'].empty_label = "انتخاب کنید"
        self.fields['job'].empty_label = "انتخاب کنید"
        self.fields['province'].empty_label = "استان را انتخاب کنید"
        self.fields['city'].empty_label = "شهر را انتخاب کنید"

        # ایمیل را فقط برای نمایش غیرفعال کنید (اختیاری)
        # self.fields['email'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        new_password_confirm = cleaned_data.get("new_password_confirm")

        if new_password and not new_password_confirm:
            self.add_error('new_password_confirm', "لطفاً تکرار کلمه عبور جدید را وارد کنید.")
        elif new_password_confirm and not new_password:
            self.add_error('new_password', "لطفاً کلمه عبور جدید را وارد کنید.")
        elif new_password and new_password_confirm and new_password != new_password_confirm:
            self.add_error('new_password_confirm', "کلمه عبور جدید و تکرار آن مطابقت ندارند.")

        email = cleaned_data.get('email')
        # این اعتبارسنجی فقط در صورتی نیاز است که فیلد ایمیل قابل ویرایش باشد
        if email and self.instance.email != email and CustomUser.objects.filter(email=email).exists():
            self.add_error('email', "این ایمیل قبلاً توسط کاربر دیگری ثبت شده است.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.cleaned_data.get("new_password"):
            user.set_password(self.cleaned_data["new_password"])

        if commit:
            user.save()
        return user