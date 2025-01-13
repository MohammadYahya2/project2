# courses/models.py

from django.db import models
from django.contrib.auth.models import User

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
    name = models.CharField(max_length=100)

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

# courses/models.py

from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='instructors/', null=True, blank=True)  # جعل الحقل اختياريًا
    designation = models.CharField(max_length=100, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name





class Course(models.Model):
    # الحقول الحالية...
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating_count = models.IntegerField(default=0)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    duration = models.FloatField()
    students_count = models.IntegerField(default=0)
    delay = models.FloatField(default=0.1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    
    # الحقول الجديدة
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title




class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

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