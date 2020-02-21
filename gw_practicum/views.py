from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Homepage")

def student(request):
    response = "Student Homepage"
    return HttpResponse(response)

def studentPlan(request, projectplan_id='None'):
    response = "Student Project Plan Form"
    return HttpResponse(response)

def studentMidpoint(request, midpointevaluation_id='None'):
    response = "Student Midpoint Evaluation"
    return HttpResponse(response)

def studentSelfEvaluation(request, selfevaluation_id='None'):
    response = "Student Self Evaluation"
    return HttpResponse(response)

def studentSelfEvaluation(request, selfevaluation_id='None'):
    response = "Student Self Evaluation"
    return HttpResponse(response)

def preceptorSelfEvaluation(request, preceptor_evaluation_id='None'):
    response = "Student Preceptor Evaluation"
    return HttpResponse(response)
