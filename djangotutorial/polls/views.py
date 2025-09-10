from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("You are at the polls index")
# Create your views here.
def detail(request, question_id): 
    return HttpResponse(f"You are looking at question {question_id}.")
def results(request, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response % question_id)