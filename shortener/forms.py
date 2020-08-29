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
                        "placeholder": "Long URL",
                        "class": "form-control"
                        }
                )
            )
    # def clean(self):
    #     super(SubmitUrlForm, self).clean()
    #     # url = cleaned_data["url"]
    #     # print(url)
    # def clean_url(self):
    #     print("self.cleaned_data = ", self.cleaned_data)
    #     url = self.cleaned_data['url'] #cleaned_data is a Django Form's thing!
    #     print(url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field!")
    #     return url