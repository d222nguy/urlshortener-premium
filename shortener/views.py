from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import URL
from .forms import SubmitUrlForm
from .utils import addHttpIfNecessary, checkForMalware
from analytics.models import ClickEvent
# Create your views here.
def test_view(request):
    return HttpResponse("some stuff")
def url_redirect_view(request, shortcode = None, *args, **kwargs):
    print(request.method)
    obj = get_object_or_404(URL, shortcode = shortcode)
    return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            'title': "URL Shortener",
            'form': the_form
        }
        # print(context)
        return render(request, "shortener/home.html", context)
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {"form": form}
        template = "shortener/home.html"
        if form.is_valid():
            print("Form is valid!")
            new_url = addHttpIfNecessary(form.cleaned_data["url"]) #Get url from submitted form
            print("new_url = ", new_url)
            try:
                obj, created = URL.objects.get_or_create(url = new_url) #create model object
                check = checkForMalware(new_url)
            except: #primarily to catch MultipleObjectreturned error
                obj, created = URL.objects.filter(url = new_url).first(), False
                template = "shortener/already-exists.html"
            context = {
                "object": obj,
                "created": created
            }
            if check:
                template =  "shortener/suspicious.html"
            elif created:
                template = "shortener/success.html"
            elif not created:
                template = "shortener/already-exists.html"

            print(form.cleaned_data)
        #context = {"form": form}
        return render(request, template, context)
class URLRedirectView(View):
    def get(self, request, shortcode = None, *args, **kwargs):
        print("shortcode = ", shortcode)
        obj = get_object_or_404(URL, shortcode = shortcode)
        print("obj url = ", obj.url)
        ClickEvent.objects.create_event(obj)
        toret = HttpResponseRedirect(obj.url)
        print(toret)
        return toret
    def post(self, request, *args, **kwargs):
        return HttpResponse()