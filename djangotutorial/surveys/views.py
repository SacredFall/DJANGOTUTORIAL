from django.shortcuts import render, get_object_or_404
from . models import Topic

def index(request):
    latest_survey_list = Topic.objects.all()[:5]
    context = {"latest_survey_list": latest_survey_list}
    return render(request, "surveys/index.html", context)
def details(request, survey_id):
    context = (f"You are on survey: {survey_id}")
    return render(request,"surveys/details.html",context)

def results(request,survey_id):
    context = (f"The results of survey {survey_id}")
    return render(request, "surveys/results.html", context)