from django.shortcuts import render , redirect , get_object_or_404 
from .form import *
from .models import *
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging 
from django.contrib import messages
# Create your views here.

def index (request):
    return render(request, 'web/index.html')

def register (request):
    form = CraeteUserForm()
    if request.method == "POST":
     form = CraeteUserForm(request.POST)
     if form.is_valid():
        form.save()
        messages.success(request,'register success')
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
           messages.success(request,'Login success')
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
            messages.success(request,'create success')
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


@login_required(login_url='login')
def update_record(request,record_id):
    record = get_object_or_404(Record, id=record_id)
    form = UpdateRecord(instance=record)
    if request.method == "POST":
        form = UpdateRecord(request.POST,instance=record) 
        if form.is_valid():
            form.save()
            messages.success(request,'update success')
            return redirect("dashboard")
            
    context ={'form' : form}
    
    return render (request,"web/Update_Record.html", context=context)
    
@login_required(login_url='login')    
def delete_record(request,record_id):
    record = get_object_or_404(Record, id=record_id)
    record.delete()
    messages.success(request,'delete success')
    return redirect("dashboard")

logger =logging.getLogger(__name__)

@login_required(login_url='login')    
def search_quary(request):
    quary = request.GET.get('quary')
    results =[]
    try:
        if quary:
            results  = Record.objects.filter(
                Q(frist_name__icontains=quary) |
                Q(id__icontains=quary) |
                Q(tall__icontains=quary)
                )
    except Exception as e:
         logger.error("Erorr during search %s ",e )

    return render(request, 'web/search.html', context={'results' : results , 'quary' : quary})


def LogoutUser(request):
    logout(request)
    messages.success(request,'logout success')
    return redirect('login')

def Erorr_page(request,exception):
    return render(request,'web/404.html',status=404)
    
