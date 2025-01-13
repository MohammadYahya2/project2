# courses/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm, CourseForm, DesignerConsultationForm, ContactForm
from .models import Course, Category, DesignerConsultation, Instructor, Carousel, Service, About, Testimonial, Contact
from django.contrib.auth.views import LoginView, LogoutView
# 1. الصفحة الرئيسية
def home(request):
    categories = Category.objects.all()
    carousels = Carousel.objects.all()
    services = Service.objects.all()
    about = About.objects.first()
    instructors = Instructor.objects.all()
    testimonials = Testimonial.objects.all()
    
    # جلب الكورسات
    courses = Course.objects.all()

    # افترض أن لديك متغير gallery_images
    gallery_images = []  # قم بتعريفه أو جلبه حسب الحاجة

    context = {
        'categories': categories,
        'carousels': carousels,
        'services': services,
        'about': about,
        'instructors': instructors,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
        'courses': courses,  # إضافة الكورسات إلى السياق
    }
    return render(request, 'courses/home.html', context)

# 2. صفحة تسجيل المستخدم
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'مرحبا {user.first_name}! تم إنشاء حسابك بنجاح.')
            return redirect('home')
        else:
            messages.error(request, 'هناك خطأ في البيانات المدخلة. يرجى المحاولة مرة أخرى.')
    else:
        form = UserRegisterForm()
    return render(request, 'courses/register.html', {'form': form})

# 3. تسجيل الدخول باستخدام عارض Django المخصص
class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'courses/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'مرحبا {form.get_user().username}! تم تسجيل الدخول بنجاح.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
        return super().form_invalid(form)

# 4. تسجيل الخروج باستخدام عارض Django المدمج
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'تم تسجيل الخروج بنجاح.')
        return super().dispatch(request, *args, **kwargs)

# 5. إضافة كورس جديد
@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user  # تأكد من وجود حقل created_by في نموذج Course
            course.save()
            messages.success(request, f'تم إضافة الكورس "{course.title}" بنجاح.')
            return redirect('home')
        else:
            messages.error(request, 'هناك خطأ في البيانات المدخلة. يرجى المحاولة مرة أخرى.')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

# 6. تفاصيل الكورس
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

# 7. طلب استشارة
@login_required
def request_consultation(request):
    if request.method == 'POST':
        form = DesignerConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()
            messages.success(request, 'تم إرسال طلب الاستشارة بنجاح.')
            return redirect('home')
        else:
            messages.error(request, 'هناك خطأ في البيانات المدخلة. يرجى المحاولة مرة أخرى.')
    else:
        form = DesignerConsultationForm()
    return render(request, 'courses/request_consultation.html', {'form': form})

# 8. عرض الكورسات بناءً على الفئة
def courses_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    courses = Course.objects.filter(category=category)
    categories = Category.objects.prefetch_related('sub_categories').all()
    context = {
        'courses': courses,
        'categories': categories,
        'selected_category': category
    }
    return render(request, 'courses/home.html', context)
def about(request):
    about_info = About.objects.first()  # افتراضياً، هناك سجل واحد لـ About
    context = {
        'about_info': about_info
    }
    return render(request, 'courses/about.html', context)
def courses_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)

def team(request):
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors
    }
    return render(request, 'courses/team.html', context)

def testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'courses/testimonial.html', context)
# عرض صفحة "اتصل بنا"
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال رسالتك بنجاح. شكرًا لتواصلك معنا!')
            return redirect('home')
        else:
            messages.error(request, 'هناك خطأ في البيانات المدخلة. يرجى المحاولة مرة أخرى.')
    else:
        form = ContactForm()
    return render(request, 'courses/contact.html', {'form': form})