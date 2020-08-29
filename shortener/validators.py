from django import forms 
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .utils import addHttpIfNecessary
def validate_url(value):
    url_validator = URLValidator()
    value = addHttpIfNecessary(value)
    print("value = ", value)
    try:
        url_validator(value)
    except:
        raise ValidationError('Invalid URL!')
    return value
