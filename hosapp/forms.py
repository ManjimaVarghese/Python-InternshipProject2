from django import forms
from .models import DoctorUpload
from .models import userForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm






class CreateUserForm(UserCreationForm):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    DOCTOR_CHOICES = [('Dr.Aparna', 'Dr.Aparna'), ('Dr.Archana', 'Dr.Archana'), ('Dr.Amal', 'Dr.Amal')]
   
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    disease = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    doctor = forms.ChoiceField(choices=DOCTOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
 

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2','fullname','age','mobile','gender','disease','doctor')



class CreateUserFormNew(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))



class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2','fullname','department','mobile')


class DataFormNew(forms.ModelForm):

    # DOCTOR_CHOICES = [('Dr.Aparna', 'Dr.Aparna'), ('Dr.Archana', 'Dr.Archana'), ('Dr.Amal', 'Dr.Amal')]

    
    # Dr_name = forms.ChoiceField(choices=DOCTOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
   
    Patient_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    profile = forms.FileInput()
   
  
    class Meta:
        model = DoctorUpload
        fields = ('Patient_name','profile')





class CreateUserFormNewOne(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    

class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')







