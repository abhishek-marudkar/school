from main.models import School, Students
from django import forms


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('name', 'enrollment', 'school',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollment': forms.NumberInput(attrs={'class': 'form-control'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
        }
