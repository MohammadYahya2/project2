# courses/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Course, DesignerConsultation
from .models import Course, DesignerConsultation, Contact, Curriculum, Lesson
from .models import Course, Testimonial

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
        fields = [
            'title', 'description', 'price', 'instructor', 'duration',
            'students_count', 'rating_count', 'image', 'video_url',
            'requirements', 'objectives', 'what_you_learn',
            'course_includes', 'related_topics', 'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'instructor': forms.Select(attrs={'class': 'form-select'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'students_count': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'rating_count': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
            'requirements': forms.TextInput(attrs={'class': 'form-control'}),
            'objectives': forms.TextInput(attrs={'class': 'form-control'}),
            'what_you_learn': forms.TextInput(attrs={'class': 'form-control'}),
            'course_includes': forms.TextInput(attrs={'class': 'form-control'}),
            'related_topics': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
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
class TestimonialForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Rating',
        help_text='Select a rating between 1 and 5.'
    )

    class Meta:
        model = Testimonial
        fields = ['client_name', 'profession', 'text', 'rating', 'image']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Profession'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here...', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }