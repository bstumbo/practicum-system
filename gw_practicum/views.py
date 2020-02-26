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


# Create your views here.

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
        student = Student.objects.all().filter(user_data_id=user.id).first()
        context = {
            'name': user.get_full_name(),
            'plans': PracticumPlan.objects.all().filter(student_id=student.id)
        }
        return render(request, 'student/index.html', context)
    else:
        return redirect('login')

def studentPlan(request, projectplan_id='None'):
    if request.method == 'POST':
        submittedForm = StudentPlanForm(request.POST)
        # submittedForm.student = request.user.id
        # submittedForm.preceptor = Preceptor.objects.all().filter(user_data__username=request.POST['preceptor']).first()
        # submittedForm.site = Site.objects.all().filter(name=request.POST['site']).first()
        # submittedForm.practicum_director = PracticumDirector.objects.all().filter(
        #     user_data__username=request.POST['practicum_director']).first()
        if submittedForm.is_valid():
            submittedForm.save()
            return HttpResponseRedirect('/student')
    else:
        form = StudentPlanForm()
    return render(request, 'student/projectplan.html', {'form': form})

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
