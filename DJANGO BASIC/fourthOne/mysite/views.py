from django.shortcuts import render
# from django.http import HttpResponserfrom .models import Question, Choice
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


# Create your views here.
class ListQuestion(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self,request,format=None):
        questions = [question.question_text for question in Question.objects.all()]
        return Response(questions)

def hello_world(request):
    return Response({"message":"Hello,world"})

class ListQuestionApiview(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def index(request):
    question = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'mysite/index.html', {'question': question})


def page(request, question_id):
    question = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'mysite/page.html', {'question': question, 'question_id': question_id})
