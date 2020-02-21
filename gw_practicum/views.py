from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

# Create your views here.

def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'general/index.html')
    else:
        return redirect('login')

"""
    STUDENT VIEWS
"""

def student(request):
    response = "Student Homepage"
    return render(request, 'student/index.html')

def studentPlan(request, projectplan_id='None'):
    response = "Student Project Plan Form"
    return HttpResponse(response)

def studentMidpoint(request, midpointevaluation_id='None'):
    response = "Student Midpoint Evaluation"
    return HttpResponse(response)

def studentSelfEvaluation(request, selfevaluation_id='None'):
    response = "Student Self Evaluation"
    return HttpResponse(response)

def preceptorSelfEvaluation(request, preceptor_evaluation_id='None'):
    response = "Student Preceptor Evaluation"
    return HttpResponse(response)

"""
    PRECEPTOR VIEWS
"""

def preceptorSelfEvaluation(request, preceptor_evaluation_id='None'):
    response = "Student Preceptor Evaluation"
    return HttpResponse(response)

def preceptor(request):
    response = "Preceptor Homepage"
    return HttpResponse(response)

def preceptorPracticumPlanApproval(request, practicum_plan_id):
    response = "Preceptor Practicum Plan Approval"
    return HttpResponse(response)

def preceptorMidpointApproval(request, midpointevaluation_i):
    response = "Preceptor Midpoint Evaluation Approval"
    return HttpResponse(response)

def preceptorFinalEvalution(request, preceptor_final_evaluation_id):
    response = "Preceptor Practicum Plan Approval"
    return HttpResponse(response)

"""
    PRACTICUM DIRECTOR VIEWS
"""

def practicumDirector(request):
    response = "Practicum Director Homepage"
    return HttpResponse(response)

def practicumDirectorPlanApproval(request, projectplan_id):
    response = "Practicum Director Plan Approval"
    return HttpResponse(response)

def practicumMidpointEvaluationApproval(request, midpointevaluation_id):
    response = "Practicum Director Midpoint Evaluation Approval"
    return HttpResponse(response)

def practicumFinalEvaluationApproval(request, finalevaluation_id):
    response = "Practicum Director Final Evaluation Approval"
    return HttpResponse(response)

def siteRegistrationApproval(request, reg_id):
    response = "PD Site Approval"
    return HttpResponse(response)

def preceptorRegistrationApproval(request, reg_id):
    response = "PD Preceptor Approval"
    return HttpResponse(response)
