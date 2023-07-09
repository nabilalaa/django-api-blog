from operator import contains
from turtle import title
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *


def posts(request):
    data = Article.objects.all()
    response = {
        "articles": list(data.values())
    }
    return JsonResponse(response)


def post(request, slug):

    data = Article.objects.filter(title__contains=slug)
    print(data)
    response = {
        "article": list(data.values())
    }
    return JsonResponse(response)
