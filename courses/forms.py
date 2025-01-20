# courses/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Course, DesignerConsultation
from .models import Course, DesignerConsultation, Contact, Curriculum, Lesson

class UserRegisterForm(UserCreationForm):
    """
    نموذج تسجيل المستخدم الجديد.
    يضيف حقول الاسم الأول، الاسم الثاني، والبريد الإلكتروني إلى نموذج التسجيل الأساسي.
    """
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='الاسم الأول',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأول'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='الاسم الثاني',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الثاني'})
    )
    email = forms.EmailField(
        max_length=254,
        help_text='البريد الإلكتروني',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='اسم المستخدم',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'})
    )
    password1 = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'}),
        help_text='يجب أن تكون كلمة المرور على الأقل 8 أحرف.'
    )
    password2 = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'}),
        help_text='أدخل نفس كلمة المرور للتأكيد.'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    """
    نموذج تسجيل الدخول للمستخدمين.
    يستخدم البريد الإلكتروني واسم المستخدم وكلمة المرور.
    """
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم أو البريد الإلكتروني'}),
        label='اسم المستخدم أو البريد الإلكتروني'
    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'image', 'price', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان الكورس'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'وصف الكورس',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'السعر'
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'رابط الفيديو التعريفي (YouTube، Vimeo)'
            }),
        }


class DesignerConsultationForm(forms.ModelForm):
    """
    نموذج طلب استشارة من المصمم الداخلي.
    يشمل الموضوع، الرسالة، وتاريخ ووقت الاستشارة.
    """
    scheduled_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        label='تاريخ ووقت الاستشارة'
    )

    class Meta:
        model = DesignerConsultation
        fields = ['subject', 'message', 'scheduled_at']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع الاستشارة'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'اكتب رسالتك هنا...',
                'rows': 5
            }),
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسمك'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'بريدك الإلكتروني'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الموضوع'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'رسالتك'}),
        }
class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان المنهج الدراسي'
            }),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان الدرس'
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'رابط الفيديو (YouTube، Vimeo)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'محتوى الدرس',
                'rows': 5
            }),
        }