from rest_framework import serializers
from rest_framework.response import Response
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author']
