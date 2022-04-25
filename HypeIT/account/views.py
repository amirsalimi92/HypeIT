from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.http.response import HttpResponseRedirect
from .models import Staff
from .forms import SearchForm, CityForm, DepartmentForm, StaffForm
from step.models import Warehouse, Preparing, InUse



# Create your views here.

def homeView(request):

    n = 0

    statwh = Warehouse.objects.all()
    statpr = Preparing.objects.all()
    statiu = InUse.objects.all()

    for x in statwh:
        if x.status == 2:
            n += 1

    for x in statpr:
        if x.status == 1:
            n += 1
        elif x.status == 2:
            n += 1
    
    for x in statiu:
        if x.status == 1:
            n += 1
        elif x.status == 2:
            n += 1
    

    context = {
        
        'p' : n
    }

    return render(request, 'account/home.html', context) 



def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            return HttpResponseRedirect(reverse(homeView))
            #settings.LOGIN_REDIRECT_URL
        else:
            context = {
                'username' : username,
                'password' : password,
            }
            return render(request, 'account/login.html', context)
    
    else:
        return render(request, 'account/login.html', {})



def logoutView(request):
    logout(request)

    return HttpResponseRedirect(reverse(homeView))


@login_required
def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            

            return redirect(reverse(homeView))

    else:
        form = UserCreationForm()

        context = {
            'form': form,
        }

    return render(request, 'account/register.html', context)

def profileView(request):
    profile = request.user.profile

    context = {
        'Profile' : profile ,

    }

    return render(request, "account/profile.html", context)


@login_required
def staffRegisterView(request):

    submitted = False
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/extern?submitted=True')
    else:
        form = StaffForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'account/staff_register.html', {'form':form, 'submitted' : submitted})


@login_required
def staffEditView(request, staff_id):
    input = Staff.objects.get(pk = staff_id)

    if request.method == "POST":
        staffEd = StaffForm(request.POST, request.FILES, instance=input)
        if staffEd.is_valid():
            staffEd.save()
            return HttpResponseRedirect(reverse(staffView))
            ######### bayad reverse bejaye reversed be kar beravad!
    else:
        staffEd = StaffForm(instance=input)

    context = {
        'form' : staffEd,
    }

    return render(request, 'account/staff_edit.html', context)


def staffView(request):
    staff = Staff.objects.all()


    context = {
        'staff' : staff,
    }

    return render(request, "account/staff.html", context) 



def searchStaffView(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        staff = Staff.objects.filter(lName__contains = searched)

        context = {
            'staff' : staff,
            'searched' : searched
        }

        return render(request, "account/staff.html", context)
    else:
        staff = Staff.objects.all()
        return render(request, "account/staff.html", {'staff' : staff})


def staffDeleteView(request, staff_id):
    input = Staff.objects.get(pk = staff_id)
    if request.method == 'POST':
        input.delete()
        return HttpResponseRedirect(reverse(staffView))
    else:
        return HttpResponseRedirect(reverse(staffView))