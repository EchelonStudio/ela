from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question
 


def index(request):
    latest_question_list = Question.objects.order_by("-published_date")[:5]

    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse("You're looking at the result of poll %s." % question_id)


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, "polls/detail.html", {
#             "question": question,
#             "error_message": "You didnt select a choice"
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()

#         return HttpResponseRedirect(reverse("polls:results", args=(question.id)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

