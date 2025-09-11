from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
def index(request):
    latest_question_list = Question.objects.all().order_by("-pub_date")[:5]
    output = ", ".join([q.question_test for q in latest_question_list])
    return HttpResponse(f"You are at the polls index. Latest questions are: {output}")
# Create your views here.
def detail(request, question_id): 
    return HttpResponse(f"You are looking at question {question_id}.")
def results(request, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)
def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}.")