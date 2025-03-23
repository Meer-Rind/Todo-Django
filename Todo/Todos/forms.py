from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task

#creating form for the registration of the user
class RegisterForm(UserCreationForm):#creating a form with the name of the RegisterForm which is extending the UserCreationForn
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    
    
    #creating meta class that will help us to link this new registerform to the user mdoel
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        
        
        
#creating login form 
class LoginForm(forms.Form):
    #creating two fields
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your username'})
    )        
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'})
    )
    
    #we are not creating anything like meta class in this becuase this don't need something like that


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task    
        fields = ['title','description','status']