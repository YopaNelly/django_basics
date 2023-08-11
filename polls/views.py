from django.shortcuts import render

fron django.template import loader

from django.http import HttpResponse

from .models import Question
def index(request):
    """
view the display    the latest 5 poll questions
in the system
"""
    latest_question_list = Question.objcts.order_by("-pub_date")[:5]
    # update the index view inpoll/views.py to use the template
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
  #  output = ", ".join([q.question_text for q in latest_question_list])

    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

