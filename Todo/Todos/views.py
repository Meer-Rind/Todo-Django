from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TodoForm

# Create your views here.

def welcome(request):
    return render(request,"Todos/welcome.html")
#creating view for the register
def Register_view(request):
    if request.method=="POST":#checking that if request.method is post or not menas that the user is going to post the form witht he filleddata
        form = RegisterForm(request.POST)#givng the form varaible with the value of the RegisterForm so that when will the user enter the value in the form it will go to post
        if form.is_valid():#chcking that if form is valid or not
            user = form.save(commit=False)#in this line we have created a new variable with the4 name of the user and give it the vlaue of the form.swave so when the user will try to save it it will save it to the memeory and the comit false will used to not save it to the database directly and firstly it wil be saverd in t he memroy 
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            messages.success(request,"Regestration Sucessful")
            return redirect('/login')
    else:
        form = RegisterForm()#now giving it a form here for the empty form means if the user will go here for the first he will see a empty form
    return render(request,'Todos/register.html',{'form':form})#render is used to render the html pages here we are using it for the render the html page and also for the rendering of the form which is given here as a dictinoary
        
            
#creating login view here
def Login_view(request):
    form = LoginForm()
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #extracting the username and password from the form and then we will autenticate it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user =  authenticate(request,username = username,password = password)
            #checking and authenticatin
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfull')
                return redirect('/Task_list')
            else:
                messages.error(request,'Invlaid Username or Password')
        else:
            form = LoginForm()
    return render(request,'Todos/login.html',{'form':form})        
            
            
            
#creating a view for showing the task or the todos
@login_required
def Task_list(request):
    tasks = Task.objects.filter(user=request.user)
    if not tasks.exists():
        messages = 'No task found Create A new task.'
    else:
        messages = None
        
    context = {
        'tasks':tasks,
        'messages':messages,
    }            
    return render(request,'Todos/Task_list.html',context)  

@login_required
def add_task(request):
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save() 
            return redirect('/Task_list')
    else:
        form = TodoForm()
    return render(request,'Todos/add_task.html',{'form':form})        



@login_required
def edit_task(request,task_id):
    task =get_object_or_404(Task,id = task_id,user = request.user)
    if request.method=="POST":
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Task_list')
    else:
        form = TodoForm(instance=task)
    return render(request,'Todos/edit_task.html',{'form':form})        
    
    
    
@login_required
def delete(request,task_id):
    task = get_object_or_404(Task,id = task_id, user=request.user)
    if request.method=="POST":
        task.delete()
        return redirect('/Task_list')
    
    return render(request,'Todos/delete.html',{'task':task})    