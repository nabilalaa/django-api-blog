from rest_framework import serializers
from .models import *


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
