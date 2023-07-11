

from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(["GET"])
def posts(request):
        data = Article.objects.all()
        serializer = ArticalSerializer(data, many=True)

        return Response(serializer.data)


def post(request, slug):

    data = Article.objects.filter(title__contains=slug)
    print(data)
    response = {
        "article": list(data.values())
    }
    return JsonResponse(response)   
    