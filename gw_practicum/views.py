from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import StudentPlanForm
from .models import PracticumPlan
from .models import Preceptor
from .models import PracticumDirector
from .models import Site
from .models import Student


def index(request):
    user = request.user
    if user.is_authenticated:
        group = {
            'Students': 'student',
            'PracticumDirectors': 'practicum-director',
            'Preceptors': 'preceptor'
        }
        section = group.get(str(user.groups.first()), '/')
        return redirect(section)
    else:
        return redirect('login')

"""
    STUDENT VIEWS
"""


def student(request):
    user = request.user
    if user.is_authenticated and str(user.groups.first()) == 'Students':
        authStudent = Student.objects.all().filter(user_data_id=user.id).first()
        context = {
            'name': user.get_full_name(),
            'plans': PracticumPlan.objects.all().filter(student_id=authStudent.id),
            'userType': 'student'
        }
        return render(request, 'student/index.html', context)
    else:
        return redirect('login')


def studentPlan(request, projectplan_id='None'):
    action = '/student/practicum-plan/' + str(projectplan_id) if projectplan_id != 'None' else '/student/practicum-plan'
    if request.method == 'POST':
        if projectplan_id != 'None':
            submittedForm = StudentPlanForm(instance=PracticumPlan.objects.get(id=projectplan_id), data=request.POST)
        else:
            submittedForm = StudentPlanForm(request.POST)
        if submittedForm.is_valid():
            submittedForm.save()
            return HttpResponseRedirect('/student')
    elif request.method == 'GET' and projectplan_id != 'None':
        form = StudentPlanForm(instance=PracticumPlan.objects.get(id=projectplan_id))
    else:
        form = StudentPlanForm()
    return render(request, 'student/projectplan.html', {'form': form, 'action': action})


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


def preceptor(request):
    user = request.user
    if user.is_authenticated and str(user.groups.first()) == 'Preceptors':
        authPreceptor = Preceptor.objects.all().filter(user_data_id=user.id).first()
        allPlans = PracticumPlan.objects.all().filter(preceptor_id=authPreceptor.id)
        context = {
            'name': user.get_full_name(),
            'pendingPlans': allPlans.all().filter(preceptor_approval=None, pd_approval=True),
            'activePlans': allPlans.all().filter(preceptor_approval=True, pd_approval=True),
            'userType': 'preceptor'
        }
        return render(request, 'preceptor/index.html', context)
    else:
        return redirect('login')


def preceptorPracticumPlanApproval(request, practicumplan_id):
    studentPlan = PracticumPlan.objects.get(id=practicumplan_id)
    if 'approve' in request.get_full_path():
        studentPlan.preceptor_approval = True
        studentPlan.save()
        return HttpResponseRedirect('/preceptor')
    else:
        return render(request, 'preceptor/projectplanapproval.html', {'plan': studentPlan})


def preceptorMidpointApproval(request, midpointevaluation_i):
    response = "Preceptor Midpoint Evaluation Approval"
    return HttpResponse(response)


def preceptorFinalEvalution(request, preceptor_final_evaluation_id):
    response = "Preceptor Practicum Plan Approval"
    return HttpResponse(response)


def preceptorSelfEvaluation(request, preceptor_evaluation_id='None'):
    response = "Student Preceptor Evaluation"
    return HttpResponse(response)

"""
    PRACTICUM DIRECTOR VIEWS
"""


def practicumDirector(request):
    user = request.user
    if user.is_authenticated and str(user.groups.first()) == 'PracticumDirectors':
        authPD = PracticumDirector.objects.all().filter(user_data_id=user.id).first()
        allPlans = PracticumPlan.objects.all().filter(practicum_director=authPD.id)
        context = {
            'name': user.get_full_name(),
            'pendingPlans': allPlans.all().filter(pd_approval=None),
            'pendingPreceptor': allPlans.all().filter(preceptor_approval=None, pd_approval=True),
            'activePlans': allPlans.all().filter(preceptor_approval=True, pd_approval=True),
            'userType': 'practicum director'
        }
        return render(request, 'practicum-director/index.html', context)
    else:
        return redirect('login')


def practicumDirectorPlanApproval(request, projectplan_id):
    studentPlan = PracticumPlan.objects.get(id=projectplan_id)
    # Update student's plan
    if request.method == 'POST':
        submittedForm = StudentPlanForm(instance=PracticumPlan.objects.get(id=projectplan_id), data=request.POST)
        if submittedForm.is_valid():
            submittedForm.save()
            return HttpResponseRedirect('/practicum-director')
    # Approve Student Plan
    if 'pdapprove' in request.get_full_path() and str(request.user.groups.first()) == 'PracticumDirectors':
        studentPlan.pd_approval = True
        studentPlan.save()
        return HttpResponseRedirect('/practicum-director')
    elif 'precepapprove' in request.get_full_path() and str(request.user.groups.first()) == 'PracticumDirectors':
        studentPlan.preceptor_approval = True
        studentPlan.save()
        return HttpResponseRedirect('/practicum-director')
    # Access Student Plan
    else:
        form = StudentPlanForm(instance=PracticumPlan.objects.get(id=projectplan_id))
        return render(request, 'practicum-director/projectplan.html', {'form': form, 'plan': studentPlan, 'userType': 'practicum director'})


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

# HOURS TRACKING VIEWS
def hours(request, projectplan_id):
    response = "hours added"
    return render(request, 'general/trackhours.html')

def addHours(request):
    return HttpResponseRedirect('/student')

def removeHours(request):
    return HttpResponseRedirect('/student')