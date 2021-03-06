# Generated by Django 2.2.3 on 2019-07-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=220, unique=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('admin', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False, verbose_name='Student Status')),
                ('instructor', models.BooleanField(default=False, verbose_name='Teacher Status')),
                ('staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
