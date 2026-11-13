from django.shortcuts import render  # type: ignore[import-untyped]
from django.http import HttpResponse  # type: ignore[import-untyped]
from django.views import View  # type: ignore[import-untyped]
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, Universe!")
    