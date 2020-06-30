from django.shortcuts import render,redirect
from django.http import HttpResponse

from . forms import CreateUserForm  
def dashboard(request):
    context={}
    return render(request,'dashboard.html',context)
# Create your views here.
def login(request):
    context={}
    return render(request,'login.html',context)
def signin(request):
    form=CreateUserForm()
    if request.method == 'POST' :
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={'form':form}
    
    return render(request,'signin.html',context)