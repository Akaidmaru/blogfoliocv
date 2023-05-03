from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    name = request.GET.get("name") or "world"
    return HttpResponse(f'Hello, {name}!')
