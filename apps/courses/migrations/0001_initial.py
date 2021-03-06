# Generated by Django 2.2.3 on 2019-07-22 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=254)),
                ('course_slug', models.CharField(blank=True, max_length=124)),
                ('course_details', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('course_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course Packages',
                'verbose_name_plural': 'Course Packages',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=167)),
                ('description', models.TextField()),
                ('module_code', models.CharField(blank=True, max_length=120)),
                ('resource', models.FileField(upload_to='<django.db.models.fields.CharField>/', verbose_name='Learning Resouce')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('course_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CoursePackage')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
                'ordering': ['-date_added'],
            },
        ),
    ]
