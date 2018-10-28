from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models import Owner 
from base.forms import OwnerForm
# Create your views here.

def new_owner(request):
    form = OwnerForm()
    context={
        'form': form
    }
    return render(request, 'owner/new.html', context)

def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        form.save()

def index_owner(request):
    owners = Owner.objects.all().values()
    context={
        'owners': owners
    }
    return render(request, 'owner/index.html', context)

def delete_owner(request, owner_id):
    if request.method == 'POST':
        owner = Owner.objects.get(id=owner_id)
        owner.delete()
        print('Dueño borrado satisfactoriamente')
        return redirect('index_owner')
    else:
        print('Dueño no a sido borrado')
        return redirect('index_owner')

def edit_owner(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    form = OwnerForm(instance=owner)
    context={
        'form': form,
        'owner': owner
    }
    return render(request, 'owner/edit.html', context)

def update_owner(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        form.save()
        return redirect('index_owner')


