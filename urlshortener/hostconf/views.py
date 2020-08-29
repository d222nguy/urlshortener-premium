from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_URL_REDIRECT = getattr(settings, "DEFAULT_REDIRECT_URL", "")


def wildcard_redirect(request, path = None):
    print("path = ", path)
    new_url = DEFAULT_URL_REDIRECT
    if path:
        new_url = DEFAULT_URL_REDIRECT + "/" + path
    print("new_url = ", new_url)
    return HttpResponseRedirect(new_url)
