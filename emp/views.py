from django.shortcuts import render ,HttpResponse
from .models import Emp
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def dashbord(request):
    return render(request, 'dashbord.html') 

def index(request):
    return render(request, 'index.html') 
    
def all_emp(request):
     emps=Emp.objects.all()
     context={
        "emps": emps
     }
     return render(request, 'all_emp.html',context) 
    
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = int(request.POST['phone'])
        # e=Emp() 
        # e.first_name=f_name 
        # e.last_name=l_name
        # e.phone_number=phone
        # print(e.first_name)
        e=Emp(first_name=first_name,last_name=last_name,phone_number=phone_number)
        e.save()
        messages.add_message(request, messages.INFO, "Employ add successfully!!")
        return redirect('all_emp')
    elif request.method == 'GET':
        return render(request, 'add_emp.html') 
    else:
        return HttpResponse("Employee has not been added !! ")


def del_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_del=Emp.objects.get(id=emp_id)
            emp_del.delete()
            return HttpResponse("Successfully Deleted!!")
        except:
            return HttpResponse("Please enter a valid emp id")
    
    emps=Emp.objects.all()
    context={
        "emps": emps
     }
    return render(request, 'del_emp.html', context) 

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']

        emps = Emp.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
    
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')

def update_emp(request):
    return render(request, 'update_emp.html') 

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        userpass = request.POST['userpassword1']
        user=authenticate(request,username=username,password=userpass)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("credentials Invalid!!")
    return render(request, 'login_page.html') 

def registration_page(request):
    if request.method == 'POST':
        uname=request.POST['username']
        uemail=request.POST['useremail']
        upassword1=request.POST['userpassword1']
        upassword2=request.POST['userpassword2']
        if(upassword1!=upassword2):
            return HttpResponse("password and confirm password not same!!")
        my_user=User.objects.create_user(uname,uemail,upassword1)
        return redirect('/login_page')
    return render(request, 'registration_page.html') 



def logout_page(request):
    logout(request)
    return redirect('/login_page')
