# Generated by Django 4.2.7 on 2025-01-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_remove_instructor_facebook_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
