from django import forms
from .models import Department
from .models import Site
from .models import Preceptor
from .models import PracticumDirector
from .models import PracticumPlan
from .models import Hours


class StudentPlanForm(forms.ModelForm):
    class Meta:
        model = PracticumPlan
        exclude = ['preceptor_approval', 'pd_approval', 'total_hours']


class TrackHoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = '__all__'
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'practicum': forms.HiddenInput(),
            'student': forms.HiddenInput()
        }
