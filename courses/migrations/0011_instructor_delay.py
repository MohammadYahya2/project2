# courses/migrations/0011_instructor_delay.py

from django.db import migrations, models

def create_or_update_default_instructor(apps, schema_editor):
    Instructor = apps.get_model('courses', 'Instructor')
    instructor, created = Instructor.objects.get_or_create(
        id=1,
        defaults={
            'name': 'Default Instructor',
            'image': 'instructors/Purple_and_White_Modern_Marketing_Service_Instagram_Post.jpg',  # تأكد من وجود الصورة في `media/instructors/`
            'designation': 'Default Designation',
            'facebook_url': 'https://facebook.com/mohammad1',
            'twitter_url': 'https://twitter.com/mohammad1',
            'instagram_url': 'https://instagram.com/mohammad1',
            'delay': 0.1,
        }
    )
    if not created:
        # تحديث الحقول إذا كان المدرس موجودًا
        instructor.name = 'Default Instructor'
        instructor.image = 'instructors/Purple_and_White_Modern_Marketing_Service_Instagram_Post.jpg'
        instructor.designation = 'Default Designation'
        instructor.facebook_url = 'https://facebook.com/mohammad1'
        instructor.twitter_url = 'https://twitter.com/mohammad1'
        instructor.instagram_url = 'https://instagram.com/mohammad1'
        instructor.delay = 0.1
        instructor.save()

class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_instructor_facebook_url_instructor_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='delay',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.RunPython(create_or_update_default_instructor),
    ]
