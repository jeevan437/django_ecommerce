from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from .models import Stores
from .forms import StoreForm
# Create your views here.

def home(request):
    return render(request,'base.html')
def get_stores(request):

    stores_data = Stores.objects.all()

    return render(request, "get_stores.html", {'stores_data':stores_data})

def add_stores(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            obj = Stores()
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.contact = form.cleaned_data['contact']
            obj.address = form.cleaned_data['address']
            obj.reviews = form.cleaned_data['reviews']
            obj.save()
        else:
            raise form.ValidationErrors
        return HttpResponseRedirect(reverse('success'))
    else:
        form = StoreForm()

    return render(request, 'add_stores.html', {'form': form})

def success(request):

    return render(request,"success.html",)