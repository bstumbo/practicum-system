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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('/student', views.student, name='student'),
    path('/student/practicum-plan', views.studentPlan, name='student-plan-form'),
    path('/student/practicum-plan/<int:projectplan_id>', views.studentPlan, name='student-plan'),
    path('/student/midpoint', views.studentMidpoint, name='student-midpoint-form'),
    path('/student/midpoint/<int:midpointevaluation_id', views.studentMidpoint, name='student-midpoint'),
    path('/student/self-evaluation', views.studentSelfEvaluation, name='student-self-evaluation-form'),
    path('/student/self-evaluation/<int:selfevaluation_id>', views.studentSelfEvaluation, name='student-self-evaluation'),
    path('/student/preceptor-evaluation/<int:preceptor_evaluation_id>', views.preceptorSelfEvaluation,
         name='preceptor-evaluation'),
    path('/preceptor', views.preceptor, name='preceptor'),
    path('/preceptor/practicum-plan/<int:practicum_plan_id>', views.preceptorPracticumPlanApproval,
         name='preceptor-practicum-plan-approval'),
    path('/preceptor/midpoint-evaluation/<int:midpointevaluation_id>', views.preceptorMidpointApproval,
         name='preceptor-midpoint-approval'),
    path('/preceptor/final-evaluation/<int:preceptor_final_evaluation_id>', views.preceptorFinalEvalution,
         name='preceptor-final-evaluation'),
    path('/practicum-director', view.practicum-director, name='practicum-director'),

]
