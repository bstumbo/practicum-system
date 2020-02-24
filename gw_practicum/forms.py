from django import forms
from .models import Department
from .models import Site
from .models import Preceptor
from .models import PracticumDirector
from .models import PracticumPlan


class StudentPlanForm(forms.ModelForm):
    class Meta:
        model = PracticumPlan
        exclude = ['preceptor_approval', 'pd_approval']

    # title = forms.CharField(label='Plan title', max_length=255, required=True)
    # department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department', required=True)
    # competencies = forms.CharField(label='Competencies', required=True, widget=forms.Textarea)
    # l_obj1 = forms.CharField(label='Objective 1', required=True, widget=forms.Textarea)
    # l_obj2 = forms.CharField(label='Objective 2', required=False, widget=forms.Textarea)
    # l_obj3 = forms.CharField(label='Objective 3', required=False, widget=forms.Textarea)
    # l_obj4 = forms.CharField(label='Objective 4', required=False, widget=forms.Textarea)
    # l_obj5 = forms.CharField(label='Objective 5', required=False, widget=forms.Textarea)
    # agreement = forms.BooleanField(required=True)
    # student = forms.CharField(label='Student')
    # site = forms.ModelChoiceField(queryset=Site.objects.all(), label='Site')
    # preceptor = forms.ModelChoiceField(queryset=Preceptor.objects.all(), label='Preceptor')
    # practicum_director = forms.ModelChoiceField(queryset=PracticumDirector.objects.all(), label='Practicum Director')