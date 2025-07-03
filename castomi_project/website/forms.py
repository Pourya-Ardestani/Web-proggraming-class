from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, EDUCATION_CHOICES, JOB_CHOICES  # وارد کردن مدل UserProfile و CHOICESها


# ----------------------------------------------------
# 1. فرم ثبت‌نام اولیه (برای user-signup.html)
#    این فرم هم فیلدهای User (پیش‌فرض جنگو) و هم فیلدهای خاص UserProfile رو مدیریت می‌کنه.
# ----------------------------------------------------
class CustomUserCreationForm(UserCreationForm):
    # فیلد ایمیل (که در مدل User هست و ما می‌خوایم در فرم نمایش داده بشه و اعتبار سنجی خاص خودمون رو داشته باشه)
    email = forms.EmailField(
        label="ایمیل",
        required=True,  # این فیلد اجباری است
        widget=forms.EmailInput(attrs={'class': 'input-field left-align', 'placeholder': 'ایمیل خود را وارد کنید.'})
    )

    # فیلدهای اضافی UserProfile که در مرحله اول ثبت نام جمع‌آوری می‌شن:
    full_name = forms.CharField(
        max_length=255, required=True, label="نام و نام خانوادگی",  # نام و نام خانوادگی اجباری است
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'نام کامل خود را وارد کنید'})
    )
    national_code = forms.CharField(
        max_length=10, required=False, label="کد ملی",  # اختیاری
        widget=forms.TextInput(attrs={'class': 'input-field left-align', 'placeholder': 'مثال: 0012345678'})
    )

    # فیلدهای انتخابی (Select)
    education = forms.ChoiceField(
        choices=[('', 'انتخاب کنید')] + list(EDUCATION_CHOICES),  # اضافه کردن گزینه "انتخاب کنید" به اول لیست
        required=False, label="تحصیلات (اختیاری)",  # اختیاری
        widget=forms.Select(attrs={'class': 'input-field'})
    )
    job = forms.ChoiceField(
        choices=[('', 'انتخاب کنید')] + list(JOB_CHOICES),
        required=False, label="شغل (اختیاری)",  # اختیاری
        widget=forms.Select(attrs={'class': 'input-field'})
    )
    birthday = forms.DateField(
        label="تاریخ تولد", required=False,  # اختیاری
        widget=forms.DateInput(attrs={'class': 'input-field left-align', 'type': 'date'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%d-%m-%Y']  # فرمت‌های ورودی تاریخ
    )

    class Meta(UserCreationForm.Meta):
        model = User  # این فرم به مدل User پیش‌فرض جنگو مربوطه
        # فیلدهایی که مستقیماً توسط این فرم از مدل User مدیریت می‌شن
        fields = ('username', 'email',) + UserCreationForm.Meta.fields[
                                          2:]  # password و password2 از UserCreationForm می‌اد.

    # متد __init__ رو بازنویسی می‌کنیم تا بتیم کلاس‌های CSS رو به فیلدهای پیش‌فرض UserCreationForm بدیم
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # اضافه کردن کلاس CSS و placeholder به فیلدهای username و password
        self.fields['username'].widget.attrs.update({'class': 'input-field', 'placeholder': 'نام کاربری'})
        self.fields['password'].widget.attrs.update({'class': 'input-field left-align', 'placeholder': 'رمز عبور'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'input-field left-align', 'placeholder': 'تکرار رمز عبور'})

    # متد clean_email برای اعتبار سنجی سفارشی: آیا این ایمیل قبلاً ثبت‌نام شده است؟
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت‌نام شده است.")
        return email

    # متد save رو بازنویسی می‌کنیم تا هم User و هم UserProfile رو ذخیره کنه
    def save(self, commit=True):
        user = super().save(commit=False)  # ابتدا User رو بدون ذخیره نهایی ایجاد می‌کنه
        if commit:
            user.save()  # User رو ذخیره می‌کنه
            # حالا UserProfile رو با اطلاعات اضافی ایجاد و ذخیره می‌کنیم
            UserProfile.objects.create(
                user=user,  # اتصال به Userی که همین الان ساخته شد
                full_name=self.cleaned_data.get('full_name'),
                national_code=self.cleaned_data.get('national_code'),
                education=self.cleaned_data.get('education'),
                job=self.cleaned_data.get('job'),
                birthday=self.cleaned_data.get('birthday')
            )
        return user


# ----------------------------------------------------
# 2. فرم اطلاعات تکمیلی پروفایل (برای user-signup-2.html و account-info.html)
#    این فرم مستقیماً به مدل UserProfile متصله.
# ----------------------------------------------------
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # این فرم به مدل UserProfile شما مربوطه
        # فیلدهایی که می‌خوایم در این فرم نمایش داده بشن و کاربر پر کنه
        fields = ['mobile_number', 'phone_number', 'province', 'city', 'address']

        widgets = {
            'mobile_number': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'مثال: 09123456789'}),
            'phone_number': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'مثال: 02155555555'}),
            # برای province و city اگر لیست ثابتی از استان‌ها/شهرها دارید، باید اینجا به choices اضافه کنید.
            # در غیر این صورت، اینها به صورت TextInput ساده رندر میشن مگر اینکه در مدل choices داشته باشن.
            'province': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'استان'}),
            # فعلا به عنوان TextInput
            'city': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'شهر'}),  # فعلا به عنوان TextInput
            'address': forms.Textarea(
                attrs={'class': 'input-field', 'rows': 3, 'placeholder': 'آدرس کامل پستی خود را وارد کنید'}),
        }

    # متد __init__ (اگر نیاز به سفارشی‌سازی بیشتر دارید)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # اگر می‌خواید فیلدهای این فرم هم اختیاری باشند، نیازی به required=False در اینجا نیست
        # چون ModelForm به صورت خودکار از blank=True/null=True در مدل پیروی می‌کنه.
        # فقط اگر می‌خواید برای province و city گزینه‌های dropdown داشته باشید:
        # self.fields['province'].widget = forms.Select(choices=YOUR_PROVINCE_CHOICES)
        # self.fields['city'].widget = forms.Select(choices=YOUR_CITY_CHOICES)
        # که در این صورت باید YOUR_PROVINCE_CHOICES و YOUR_CITY_CHOICES رو تعریف کنید.


# ----------------------------------------------------
# 3. فرم ورود (Login Form) - معمولاً نیازی به سفارشی‌سازی زیاد نداره
# ----------------------------------------------------
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری', 'class': 'input-field'})
    )
    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'class': 'input-field'})
    )