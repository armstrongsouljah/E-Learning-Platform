import random
import string
from django.utils.text import slugify
from django.db.models import Avg


def unique_code_generator(size=6):
    chars=string.ascii_lowercase+string.digits
    return "".join(random.choice(chars) for _ in range(size))


def slug_generator(instance):
    slug = None
    if not instance.course_slug:
        slug = f"{slugify(instance.course_name)}-{unique_code_generator(size=7)}"
    return slug


def get_average_value(**kwargs):
    avg_ratings = kwargs.get('model').objects.all().filter(
        course_id=kwargs.get('course_id')
    ).aggregate(Avg('rating')).get('rating__avg')
    if avg_ratings is None:
        return 0
    else:
        return int(avg_ratings)