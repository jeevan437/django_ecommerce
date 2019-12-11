from django.conf.urls import url

from .views import get_stores,add_stores,success,home

urlpatterns = [

    url(r'home/',home),
    url(r'get_stores',get_stores, name = 'store_details'),
    url(r'add_stores',add_stores,name = 'add_stores'),
    url(r'success',success,name='success')


]