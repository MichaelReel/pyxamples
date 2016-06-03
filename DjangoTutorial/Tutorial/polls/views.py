from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import F

# Import models
from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'
    template_name ='polls/index.html'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', 
            {
                'question'      : question,
                'error_message' : "You didn't select a choice.",
            })
    else:
        # Using F delays the read and increment until the save and pushes
        # the operation down to the db. This avoids a race condition.
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the 'Back' button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))