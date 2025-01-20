# courses/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm, CourseForm, DesignerConsultationForm, ContactForm
from .models import Course, Category, DesignerConsultation, Instructor, Carousel, Service, About, Testimonial, Contact, Curriculum, Lesson
from django.contrib.auth.views import LoginView, LogoutView
import re
from .utils import convert_video_url
from django.db.models import Q  # Import Q for complex queries
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string

def home(request):
    categories = Category.objects.all()
    carousels = Carousel.objects.all()
    services = Service.objects.all()
    about = About.objects.first()
    instructors = Instructor.objects.all()
    testimonials = Testimonial.objects.all()

    # التعامل مع استعلام البحث
    query = request.GET.get('q', '')
    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(instructor__name__icontains=query)
        ).distinct()
    else:
        courses = Course.objects.all()

    # تطبيق pagination
    paginator = Paginator(courses, 6)  # عرض 6 دورات في الصفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('courses/course_list.html', {'courses': page_obj}, request=request)
        return JsonResponse({'html': html})

    context = {
        'categories': categories,
        'carousels': carousels,
        'services': services,
        'about': about,
        'instructors': instructors,
        'testimonials': testimonials,
        'courses': page_obj,
        'query': query,
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
    def get_success_url(self):
        messages.success(self.request, f'مرحبا {self.request.user.username}! تم تسجيل الدخول بنجاح.')
        return reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
        return super().form_invalid(form)

# 4. تسجيل الخروج باستخدام عارض Django المدمج
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
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

def course_detail(request, pk):
    course = get_object_or_404(Course, id=pk)
    testimonials = course.testimonials.all()
    similar_courses = Course.objects.filter(category=course.category).exclude(id=pk)[:4]

    # Convert standard video URL to embed URL if necessary
    if course.video_url:
        course.video_url = convert_video_url(course.video_url)

    context = {
        'course': course,
        'testimonials': testimonials,
        'similar_courses': similar_courses,
        'curriculums': course.curriculums.all(),
    }
    return render(request, 'courses/course_detail.html', context)
@login_required
def add_testimonial(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        if rating and review:
            Testimonial.objects.create(
                course=course,
                client_name=request.user.username,
                profession="Student",  # Modify as needed
                text=review
            )
            # Update rating_count and students_count
            course.rating_count = (course.rating_count * course.students_count + int(rating)) / (course.students_count + 1)
            course.students_count += 1
            course.save()
            messages.success(request, 'Your testimonial has been added successfully.')
            return redirect('course_detail', pk=course.id)
        else:
            messages.error(request, 'Please fill in all fields.')
    return redirect('course_detail', pk=course.id)

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

@login_required
def profile(request):
    return render(request, 'courses/profile.html')
def convert_youtube_url(url):
    """
    Converts a standard YouTube URL to an embed URL.
    """
    youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'
    match = re.match(youtube_regex, url)
    if match:
        video_id = None
        # Extract video ID based on URL format
        if 'youtube.com' in url:
            video_id_match = re.search(r'v=([^&]+)', url)
            if video_id_match:
                video_id = video_id_match.group(1)
        elif 'youtu.be' in url:
            video_id_match = re.search(r'youtu\.be/([^?]+)', url)
            if video_id_match:
                video_id = video_id_match.group(1)
        
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
    return url