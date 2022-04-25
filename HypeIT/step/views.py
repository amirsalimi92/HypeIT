from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.http.response import HttpResponseRedirect
from .models import InUse, Preparing, Retired, Warehouse
from .forms import WarehouseForm, PrepareForm, InUseForm, RetiredForm



# Create your views here.

def warehouseView(request):
    warehouse = Warehouse.objects.all()


    context = {
        'warehouse' : warehouse,
    }

    return render(request, "step/warehouse.html", context) 


@login_required
def warehouseEditView(request, warehouse_id):
    input = Warehouse.objects.get(pk = warehouse_id)

    if request.method == "POST":
        warehouseEd = WarehouseForm(request.POST, request.FILES, instance=input)
        if warehouseEd.is_valid():
            warehouseEd.save()
            return HttpResponseRedirect(reverse(warehouseView))
            ######### bayad reverse bejaye reversed be kar beravad!
    else:
        warehouseEd = WarehouseForm(instance=input)

    context = {
        'form' : warehouseEd,
    }

    return render(request, 'step/edit/warehouse_edit.html', context)



def warehouseTaskView(request):

    ready = Warehouse.objects.filter(status = 1)

    context = {
        'ready' : ready
    }

    return render(request, 'step/task/warehouse_task.html', context)


@login_required
def warehouseRegisterView(request):

    submitted = False
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/step/list?submitted=True')
    else:
        form = WarehouseForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'step/register/warehouse_register.html', {'form':form, 'submitted' : submitted})


def searchwarehouseView(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        warehouse = Warehouse.objects.filter(serialNumber__contains = searched)

        context = {
            'warehouse' : warehouse,
            'searched' : searched
        }

        return render(request, "step/warehouse.html", context)
    else:
        warehouse = Warehouse.objects.all()

        return render(request, "step/warehouse.html", {'warehouse' : warehouse})


def preparedView(request):
    prepared = Preparing.objects.all()


    context = {
        'prepared' : prepared,
    }

    return render(request, "step/preparing.html", context) 


@login_required
def preparedEditView(request, prepared_id):
    input = Preparing.objects.get(pk = prepared_id)

    if request.method == "POST":
        preparedEd = PrepareForm(request.POST, request.FILES, instance=input)
        if preparedEd.is_valid():
            preparedEd.save()
            return HttpResponseRedirect(reverse(preparedView))
            ######### bayad reverse bejaye reversed be kar beravad!
    else:
        preparedEd = PrepareForm(instance=input)

    context = {
        'form' : preparedEd,
    }

    return render(request, 'step/edit/prepared_edit.html', context)


@login_required
def preparedRegisterView(request):

    submitted = False
    if request.method == 'POST':
        form = PrepareForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/step/prepared_list?submitted=True')
    else:
        form = PrepareForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'step/register/prepare_register.html', {'form':form, 'submitted' : submitted})



def preparedTaskView(request):

    nothing = Preparing.objects.filter(status = 1)
    not_complate = Preparing.objects.filter(status = 2)

    context = {
        'nothing' : nothing,
        'not_complete' : not_complate
    }

    return render(request, 'step/task/prepared_task.html', context)


def searchpreparedView(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        prepared = Preparing.objects.filter(domainName__contains = searched)

        context = {
            'prepared' : prepared,
            'searched' : searched
        }

        return render(request, "step/preparing.html", context)
    else:
        prepared = Preparing.objects.all()

        return render(request, "step/preparing.html", {'prepared' : prepared})


def inUseView(request):
    inuse = InUse.objects.all()


    context = {
        'inuse' : inuse,
    }

    return render(request, "step/inuse.html", context) 


@login_required
def inuseEditView(request, inuse_id):
    input = InUse.objects.get(pk = inuse_id)

    '''date = input.date
    staff = input.staff_id
    staffquery = Staff.objects.get(pk=staff)
    staffemail = staffquery.email
    staffname = staffquery.fName

    prepareid = input.Preparing_id
    preparequery = Preparing.objects.get(prepareid)
    inventoryid = preparequery.Warehouse_id
    inventoryquery = Warehouse.objects.get(pk = inventoryid)
    inventoryserial = inventoryquery.serialNumber

    sinvq = str(inventoryquery)
    sdate = str(date)

    text = 'Dear '+staffname+' ,the '+sinvq+' with the serial number: '+inventoryserial+' was given to you on '+sdate+' by the IT team.\nAlso the following settings are done for you correctly:\n-Installed the OS and updated\n-It\'s now on domain\n-The package of applications is installed\nWe hope you enjoy being in our Hype family.\nFor any request from It team, you can easy make a ticket in jira or send an email to helpdesk@hype.de\nRegard'
    '''

    if request.method == "POST":
        inuseEd = InUseForm(request.POST, request.FILES, instance=input)
        if inuseEd.is_valid():
            inuseEd.save()

            '''
            send_mail(
            'Enjoy from your new device!',
            text,
            'amir.salimi1810@gmail.com',
            [staffemail,],
            #set the setting in Settings file! dont forget
            )
            '''

            return HttpResponseRedirect(reverse(inUseView))
            ######### bayad reverse bejaye reversed be kar beravad!
    else:
        inuseEd = InUseForm(instance=input)

    context = {
        'form' : inuseEd,
    }

    return render(request, 'step/edit/inuse_edit.html', context)


@login_required
def inuseRegisterView(request):

    submitted = False
    if request.method == 'POST':
        form = InUseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/step/inuse_list?submitted=True')
    else:
        form = InUseForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'step/register/inuse_register.html', {'form':form, 'submitted' : submitted})


def inuseTaskView(request):

    nothing = InUse.objects.filter(status = 1)
    not_complate = InUse.objects.filter(status = 2)

    context = {
        'nothing' : nothing,
        'not_complete' : not_complate
    }

    return render(request, 'step/task/inuse_task.html', context)


def searchinUseView(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        inuse = Preparing.objects.filter(device__contains = searched)

        context = {
            'inuse' : inuse,
            'searched' : searched
        }

        return render(request, "step/inuse.html", context)
    else:
        inuse = InUse.objects.all()

        return render(request, "step/inuse.html", {'inuse' : inuse})


def retiredView(request):
    retired = Retired.objects.all()


    context = {
        'retired' : retired,
    }

    return render(request, "step/retired.html", context) 


@login_required
def retiredEditView(request, retired_id):
    input = Retired.objects.get(pk = retired_id)

    if request.method == "POST":
        retiredEd = RetiredForm(request.POST, request.FILES, instance=input)
        if retiredEd.is_valid():
            retiredEd.save()
            return HttpResponseRedirect(reverse(retiredView))
            ######### bayad reverse bejaye reversed be kar beravad!
    else:
        retiredEd = RetiredForm(instance=input)

    context = {
        'form' : retiredEd,
    }

    return render(request, 'step/edit/retired_edit.html', context)


@login_required
def retiredRegisterView(request):

    submitted = False
    if request.method == 'POST':
        form = RetiredForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/step/retired_list?submitted=True')
    else:
        form = RetiredForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'step/register/retired_register.html', {'form':form, 'submitted' : submitted})


def retiredIdleView(request):
    
    retired = Retired.objects.filter(status = 1)


    context = {
        'retired' : retired,
    }

    return render(request, "step/retired.html", context) 


def retiredRecycleView(request):
    
    retired = Retired.objects.filter(status = 2)


    context = {
        'retired' : retired,
    }

    return render(request, "step/retired.html", context) 


def searchretiredView(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        retired = Retired.objects.filter(device__contains = searched)

        context = {
            'retired' : retired,
            'searched' : searched
        }

        return render(request, "step/retired.html", context)
    else:
        retired = Retired.objects.all()

        return render(request, "step/retired.html", {'retired' : retired})