from django import forms 
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .validators import validate_url
class SubmitUrlForm(forms.Form):

    url = forms.CharField(
            label='', 
            validators=[validate_url],
            widget = forms.TextInput(
                    attrs ={
                        "placeholder": "Long URL (e.g. http://malware.testing.google.test/testing/malware/). Don't worry, we have basic guards to protect you from popular cyber threats.",
                        "class": "form-control"
                        }
                )
            )