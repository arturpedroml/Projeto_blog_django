from random import SystemRandom
import string
from django.utils.text import slugify

def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))

def slugify_new(text, k=5):
    return slugify(text) + random_letters(k)
