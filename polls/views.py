from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index( request ):
    latest_question_list = Question.objects.order_by('-pub_date')               # [:N] can be added in order to show last N questions added
    context = {
        'latest_question_list': latest_question_list,
    }
    return render (request, 'polls/index.html', context)



def testit( request ):                                  #every define its goin to contain a diferent webpage
    return HttpResponse("This is a test page.")



def detail ( request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results (request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)



def vote (request, question_id):
    return HttpResponse("You are voting on question %s." %question_id)