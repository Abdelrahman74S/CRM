from django.shortcuts import render , redirect , get_object_or_404
from .form import *
from .models import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index (request):
    return render(request, 'web/index.html')

def register (request):
    form = CraeteUserForm()
    if request.method == "POST":
     form = CraeteUserForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect("login")
    else:
     form = CraeteUserForm()
    
    context = {"form" : form}    
    
    return render(request,"web/register.html", context)

def LoginUser(request):
    form = LoginForm()
    if request.method == "POST":
      form = LoginForm(request, data=request.POST)
      if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request ,username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('index') 
    else:
        form = LoginForm()
    context = {"form" : form}    
    
    return render(request,"web/login.html", context)

@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request ,'web/dashbord.html',context={'records': records})

@login_required(login_url='login')    
def create_record(request):
    form = CreateRecord()
    if request.method == "POST":
        form = CreateRecord(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    
    else:
        form = CreateRecord()
        
    context = {'form' : form}
    
    return render(request,'web/create_record.html',context=context)

@login_required(login_url='login')
def view_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    context = {"record": record}
    
    return render(request, 'web/view_record.html', context=context)


def update_record(request,record_id):
    record = get_object_or_404(Record, id=record_id)
    form = UpdateRecord(instance=record)
    if request.method == "POST":
        form = UpdateRecord(request.POST,instance=record) 
        if form.is_valid():
            form.save()
            return redirect("dashboard")
            
    context ={'form' : form}
    
    return render (request,"web/Update_Record.html", context=context)
    


def LogoutUser(request):
    logout(request)
    return redirect('login')
