from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponseRedirect
from .models import Pc
from .forms import PcForm
from step.models import Warehouse

# Create your views here.

def pcView(request):
    pc = Pc.objects.all()

    context = {
        'pc' : pc
    }

    return render(request, 'device/device.html', context)


@login_required
def deviceRegisterView(request):

    submitted = False
    if request.method == 'POST':
        form = PcForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/device/list?submitted=True')
    else:
        form = PcForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'device/device_register.html', {'form':form, 'submitted' : submitted})


@login_required
def deviceEditView(request, device_id):
    input = Pc.objects.get(pk = device_id)

    if request.method == "POST":
        deviceEd = PcForm(request.POST, request.FILES, instance=input)
        if deviceEd.is_valid():
            deviceEd.save()
            return HttpResponseRedirect(reverse(pcView))
            ######### bayad reverse bejaye reversed be kar beravad!
    else:
        staffEd = PcForm(instance=input)

    context = {
        'form' : staffEd,
    }

    return render(request, 'device/device_edit.html', context)


def searchPcView(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        pc = Pc.objects.filter(nickName__contains = searched)

        context = {
            'pc' : pc,
            'searched' : searched
        }

        return render(request, "device/device.html", context)
    else:
        staff = Pc.objects.all()
        return render(request, "device/device.html", {'pc' : pc})



def finance(request):

    warehouse = Warehouse.objects.all()
    paid = 0
    
    
    for x in warehouse:
        paid += x.price

    num = 0
    for x in warehouse:
        if x.id != 0:
            num += 1


    context = {
        'paid' : paid,
        'num' : num,
    }



    return render(request, 'device/finance.html', context)