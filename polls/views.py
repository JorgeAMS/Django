from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index( request ):
    latest_question_list = Question.objects.order_by('-pub_date')               # [:N] can be added in order to show last N questions added
    #output = ', '.join([q.question_text for q in latest_question_list])template = loader.get_template('polls/index.html')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse (template.render(context, request))


def testit( request ):                                  #every define its goin to contain a diferent webpage
    return HttpResponse("This is a test page.")

def detail ( request, question_id):
    return HttpResponse("You are looking at question %s" %question_id)

def results (request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote (request, question_id):
    return HttpResponse("You are voting on question %s." %question_id)