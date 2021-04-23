from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from .serializers import QuestionSerializer


# Create your views here.

class ListQuestionApiview(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def index(request):
    question = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'mysite/index.html', {'question': question})


def page(request, question_id):
    question = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'mysite/page.html', {'question': question, 'question_id': question_id})
