from django.shortcuts import render
from .models import Question
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Create your views here.
def index(response):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ",".join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(response, 'polls/index.html', context)


def detail(response, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse("You are Looking into Page %s" % question_id)
    return render(response, 'polls/detail.html', {'question': question})


def fetch(response):
    queryset = Question.objects.all()
    context = {
        "object_list": queryset
    }
    return render(response, "polls/fetch.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
