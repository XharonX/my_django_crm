from django import forms
from .models import Employee, Department, Position



from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill shadow-sm px-4',
        'id': 'userName',
        'placeholder': 'username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded-pill shadow-sm px-4',
        'placeholder': 'password',
        'id': 'id_password',

    }))


class EmployeeCreationForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'fstName',
        'placeholder': 'first name'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'lstName',
        'placeholder': 'last name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'id_username',
        'placeholder': 'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'id_email',
        'placeholder': 'email'
    }), required=False)
    dept = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='please select a department ',widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'id_dept',
        'placeholder': 'department'
    }))
    position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label='please select a position ', widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'id_position',
        'placeholder': 'position'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'id_password',
        'placeholder': 'password'
    }))

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'email', 'dept', 'position', 'password']
        # exclude = ['']
