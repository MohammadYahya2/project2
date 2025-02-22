# Generated by Django 4.2.7 on 2025-01-20 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_instructor_delay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='video_url',
            field=models.URLField(blank=True, help_text='أدخل رابط الفيديو التعريفي (مثل YouTube أو Vimeo)', null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='courses.course'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_url', models.URLField(blank=True, help_text='رابط الفيديو (YouTube أو Vimeo)', null=True)),
                ('content', models.TextField()),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.curriculum')),
            ],
        ),
        migrations.AddField(
            model_name='curriculum',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculums', to='courses.course'),
        ),
    ]
