# Generated by Django 2.2.3 on 2019-07-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190718_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='instructor',
            field=models.BooleanField(default=False, verbose_name='As an Instructor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student',
            field=models.BooleanField(default=False, verbose_name='As a Student'),
        ),
    ]
