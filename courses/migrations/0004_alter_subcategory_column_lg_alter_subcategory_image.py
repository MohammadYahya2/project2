# Generated by Django 4.2.7 on 2025-01-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='column_lg',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(upload_to='subcategories/'),
        ),
    ]
