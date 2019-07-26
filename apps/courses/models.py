from django.db import models
from apps.accounts.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save, post_save, post_delete
from utils.helper_funcs import slug_generator, unique_code_generator, get_average_value
from django.urls import reverse
from django.conf import settings

User = getattr(settings, 'AUTH_USER_MODEL')
RATING_CHOICES = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)


class CourseModule(models.Model):
    module_name = models.CharField(max_length=167)
    description = models.TextField()
    module_code = models.CharField(blank=True, max_length=120)
    resource = models.FileField(verbose_name='Learning Resouce', upload_to=f'{module_name.name}/')
    course_package = models.ForeignKey('CoursePackage', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')
    
    def __str__(self):
        return f"{self.module_name}"

    def get_absolute_url(self):
        return reverse('course:course-detail', kwargs={'course_slug': self.course_package.course_slug})

def module_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.module_code:
        instance.module_code = unique_code_generator(size=8)


pre_save.connect(module_pre_save_receiver, sender=CourseModule)


def module_post_delete_receiver(instance, sender, *args, **kwargs):
    if instance.resource:
        instance.resource.delete(False)

post_delete.connect(module_post_delete_receiver, sender=CourseModule)


class CoursePackage(models.Model):
    course_name = models.CharField(max_length=254)
    course_author = models.ForeignKey(User, on_delete=models.CASCADE)
    course_slug = models.CharField(max_length=124, blank=True)
    course_details = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Course Packages')
        verbose_name_plural = _('Course Packages')

    def __str__(self):
        return f'{self.course_name}'

    @property
    def average_rating(self):
        return get_average_value(
            model=self.rating_set.model,
            course_id=self.pk,
            rating=self.rating_set.model.rating
        )


def course_package_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.course_slug:
        instance.course_slug = slug_generator(instance)

pre_save.connect(course_package_pre_save_receiver, sender=CoursePackage)


class Rating(models.Model):
    course = models.ForeignKey(CoursePackage, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    rated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.course_name}"

    class Meta:
        ordering  = ['-rated_at']

    def get_absolute_url(self):
        return reverse('course:course-detail', kwargs={'course_slug': self.course.course_slug})
