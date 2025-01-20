# courses/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Carousel(models.Model):
    subtitle = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel/')
    read_more_url = models.URLField(blank=True, null=True)
    join_now_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # حقل جديد

    def __str__(self):
        return self.title

class Service(models.Model):
    image = models.ImageField(upload_to='services/')  # حقل الصورة بدلاً من الأيقونة
    title = models.CharField(max_length=100)
    description = models.TextField()
    delay = models.FloatField(default=0.1)  # لتحديد تأخير التحريك

    def __str__(self):
        return self.title

class About(models.Model):
    image = models.ImageField(upload_to='about/')
    description = models.TextField()
    more_description = models.TextField()
    read_more_url = models.URLField(blank=True, null=True)
    features = models.JSONField(default=list)  # قائمة من الميزات

    def __str__(self):
        return "About Us"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategories/')
    course_count = models.IntegerField(default=0)
    column_lg = models.IntegerField(default=3)  # مثال: 3 يعني col-lg-3
    column_md = models.IntegerField(default=6)  # مثال: 6 يعني col-md-6
    delay = models.FloatField(default=0.1)  # مثال: 0.1 ثانية تأخير

    def __str__(self):
        return self.name
# courses/models.py

from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='instructors/', null=True, blank=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    delay = models.FloatField(null=True, blank=True)  # Made optional

    def __str__(self):
        return self.name
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    duration = models.IntegerField(help_text="Duration in hours")
    students_count = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='courses/')
    video_url = models.URLField(blank=True, null=True)
    requirements = models.TextField(
        help_text="Comma-separated requirements",
        null=True,  # Allows NULL in the database
        blank=True  # Allows the field to be optional in forms
    )
    objectives = models.TextField(
        help_text="Comma-separated objectives",
        null=True,
        blank=True
    )
    what_you_learn = models.TextField(
        help_text="Comma-separated learning objectives",
        blank=True,
        null=True
    )
    course_includes = models.TextField(
        help_text="Comma-separated course features",
        blank=True,
        null=True
    )
    related_topics = models.TextField(
        help_text="Comma-separated related topics",
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )

    def __str__(self):
        return self.title
class Curriculum(models.Model):
    course = models.ForeignKey(Course, related_name='curriculums', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
class Lesson(models.Model):
    curriculum = models.ForeignKey(Curriculum, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True, help_text="رابط الفيديو (YouTube أو Vimeo)")
    content = models.TextField()

    def __str__(self):
        return self.title

# تحديث نموذج Testimonial لربطه بالكورس

class Testimonial(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='testimonials',
        null=True,
        blank=True
    )
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5,
        help_text="Rating must be between 1 and 5"
    )

    def __str__(self):
        return f'Testimonial from {self.client_name}'

# إضافة نموذج DesignerConsultation
class DesignerConsultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return f'Consultation by {self.user.username} on {self.scheduled_at}'
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact from {self.name} - {self.subject}'