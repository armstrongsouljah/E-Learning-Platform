import random
import string
from django.utils.text import slugify


def unique_code_generator(size=6):
    chars=string.ascii_lowercase+string.digits
    return "".join(random.choice(chars) for _ in range(size))


def slug_generator(instance):
    slug = None
    if not instance.course_slug:
        slug = f"{slugify(instance.course_name)}-{unique_code_generator(size=7)}"
    return slug