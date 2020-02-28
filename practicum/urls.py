"""practicum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gw_practicum import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # GENERAL PATHS
    url(r'^login/$',  auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # STUDENT PATHS
    path('student', views.student, name='student'),
    path('student/practicum-plan', views.studentPlan, name='student-plan-form'),
    path('student/practicum-plan/<uuid:projectplan_id>', views.studentPlan, name='student-plan'),
    path('student/practicum-plan/<uuid:projectplan_id>/track-hours', views.hours, name='student-plan-hours'),
    path('student/midpoint', views.studentMidpoint, name='student-midpoint-form'),
    path('student/midpoint/<uuid:midpointevaluation_id', views.studentMidpoint, name='student-midpoint'),
    path('student/self-evaluation', views.studentSelfEvaluation, name='student-self-evaluation-form'),
    path('student/self-evaluation/<uuid:selfevaluation_id>', views.studentSelfEvaluation, name='student-self-evaluation'),
    path('student/preceptor-evaluation/<uuid:preceptor_evaluation_id>', views.preceptorSelfEvaluation,
         name='preceptor-evaluation'),
    # PRECEPTOR PATHS
    path('preceptor', views.preceptor, name='preceptor'),
    path('preceptor/practicum-plan/<uuid:practicum_plan_id>', views.preceptorPracticumPlanApproval,
         name='preceptor-practicum-plan-approval'),
    path('preceptor/practicum-plan/approve/<uuid:practicum_plan_id>', views.preceptorPracticumPlanApproval,
         name='preceptor-practicum-plan-approval-approve'),
    path('preceptor/midpoint-evaluation/<uuid:midpointevaluation_id>', views.preceptorMidpointApproval,
         name='preceptor-midpoint-approval'),
    path('preceptor/final-evaluation/<uuid:preceptor_final_evaluation_id>', views.preceptorFinalEvalution,
         name='preceptor-final-evaluation'),
    # PRACTICUM DIRECTOR PATHS
    path('practicum-director', views.practicumDirector, name='practicum-director'),
    path('practicum-director/practicum-plan/<uuid:projectplan_id>', views.practicumDirectorPlanApproval,
         name='practicum-director-plan-approval'),
    path('practicum-director/practicum-plan/pdapprove/<uuid:projectplan_id>', views.practicumDirectorPlanApproval,
         name='practicum-director-plan-pdapprove'),
    path('practicum-director/practicum-plan/precepapprove/<uuid:projectplan_id>', views.practicumDirectorPlanApproval,
         name='practicum-director-plan-precepapprove'),
    path('practicum-director/midpoint-evaluation/<uuid:midpointevaluation_id>', views.practicumMidpointEvaluationApproval,
         name='practicum-director-midpoint-evaluation-approval'),
    path('practicum-director/final-evaluation/<uuid:finalevaluation_id>', views.practicumFinalEvaluationApproval,
             name='practicum-director-final-evaluation-approval'),
    path('practicum-director/site/registration/<int:reg_id>', views.siteRegistrationApproval,
                 name='practicum-director-site-registration-approval'),
    path('practicum-director/preceptor/<int:reg_id>', views.preceptorRegistrationApproval,
                 name='practicum-director-preceptor-approval'),
]
