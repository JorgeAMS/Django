from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Choice, Question

def index( request ):
    latest_question_list = Question.objects.order_by('-pub_date')               # [:N] can be added in order to show last N questions added
                                                                                # setting -pub_date brings from the last to the first
                                                                                # setting pub_date brings from the first to the last
    context = {
        'latest_question_list': latest_question_list,
    }
    return render (request, 'polls/index.html', context)



def testit( request ):                                  #every define its goin to contain a diferent webpage
    return HttpResponse("This is a test page.")



def detail ( request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def vote (request, question_id):
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



def results (request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})