from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("This is firstpage contact page.we can creat this contact page succesfullu.")
