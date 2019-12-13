from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from .models import Stores
from django.db.models import Q
from .forms import StoreForm
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request,'base.html')

def get_stores(request):
    if request.method == 'GET':
        data = Stores.objects.all().order_by('id')
        search_data = request.GET.get('search_store')

        page = request.GET.get('page', 1)

        paginator = Paginator(data, 4)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        if search_data is not None:
            data = data.filter(Q(name__icontains=search_data) | Q(address__icontains = search_data ) ).order_by('id')
        return render(request, 'get_stores.html',
                      {'stores_data':data,

                       })


'''
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
'''
def add_stores(request):
    if request.method == "POST":
        data = request.POST
        task = Stores(name = data.get("name"),
                            email = data.get("email"),
                            contact = data.get("contact"),
                            address = data.get("address"),
                            reviews = data.get("reviews"),
                      )
        print(task)
        task.save()
        return redirect(get_stores)
    return render(request, "add_stores.html")

def success(request):
    return render(request,"success.html",)

def delete_store(request, pid):
    task = Stores.objects.get(id = pid)
    task.delete()
    return redirect(get_stores)
'''
def store_update(request, pid):
    store = Stores.objects.get(id = pid)
    if request.method == "post":
        data = request.POST
        store.name = data.get("name")
        store.email = data.get("email")
        store.contact = data.get("contact")
        store.address = data.get("address")
        store.reviews = data.get("reviews")
        store.save()
        return redirect(get_stores)
    return render(request, "update.html", {'store_data':store})

'''
def store_update(request, pid):
    store_id = int(pid)
    try:
        stores_data = Stores.objects.get(id = store_id)
    except Stores.DoesNotExist:
        return redirect('home')
    store_form = StoreForm(request.POST or None, instance = stores_data)
    if store_form.is_valid():
       store_form.save()
       return redirect(get_stores)
    return render(request, 'update.html', {'store_form':store_form})

