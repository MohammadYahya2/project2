# courses/migrations/0007_course_created_at_course_created_by.py

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_course_created_at_remove_course_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True),  # جعل الحقل قابلًا لأن يكون فارغًا
        ),
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True),
        ),
    ]
