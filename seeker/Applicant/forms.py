from django import forms
from django.contrib.auth.forms import  UserCreationForm
from Applicant.models import Apply_Job
from Recruter.models import Add_Jobs

class JobForm(forms.ModelForm):
        class Meta:
                    model=Add_Jobs

                    exclude=("company","created_date","active_status")
                    widgets={
                    "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
                    "description": forms.TextInput(attrs={"class": "form-control "}),

                    }

