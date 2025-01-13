# courses/urls.py

from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('add-course/', views.add_course, name='add_course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('request-consultation/', views.request_consultation, name='request_consultation'),
    path('category/<int:category_id>/', views.courses_by_category, name='courses_by_category'),
    path('about/', views.about, name='about'),  # نمط URL لصفحة "عن الموقع"
    path('courses/', views.courses_list, name='courses'),  # نمط URL لصفحة "الكورسات"
    path('team/', views.team, name='team'),  # نمط URL لصفحة "فريق العمل"
    path('testimonial/', views.testimonial, name='testimonial'),  # نمط URL لصفحة "التوصيات"
    path('contact/', views.contact, name='contact'),  # نمط URL لصفحة "اتصل بنا"
    # يمكنك إضافة أنماط URL الأخرى مثل 'error' إذا كنت تنوي التعامل مع عرض مخصص
]
