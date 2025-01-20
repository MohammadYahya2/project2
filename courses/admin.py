# courses/admin.py

from django.contrib import admin
from .models import (
    Carousel, Service, About, Category, SubCategory, Course,
    Instructor, Testimonial, DesignerConsultation, Contact,
    Curriculum, Lesson
)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rating_count', 'instructor', 'duration', 'students_count', 'delay', 'category', 'created_at', 'created_by', 'video_url')
    search_fields = ('title', 'instructor__name', 'category__name', 'created_by__username')
    list_filter = ('instructor', 'category', 'created_at', 'created_by')

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'curriculum', 'video_url')
    search_fields = ('title', 'curriculum__title')
    list_filter = ('curriculum',)

# التسجيلات الأخرى كما هي
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at')
    search_fields = ('title', 'subtitle')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'delay')
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'course_count', 'column_lg', 'column_md', 'delay')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession', 'course')
    search_fields = ('client_name', 'profession', 'course__title')
    list_filter = ('course',)

@admin.register(DesignerConsultation)
class DesignerConsultationAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'scheduled_at')
    search_fields = ('user__username', 'subject')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('submitted_at',)
