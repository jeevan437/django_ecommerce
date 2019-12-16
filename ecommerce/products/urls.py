from django.conf.urls import url

from .views import get_stores,add_stores,success,home,delete_store,store_update,\
    GetProducts,AddProducts

urlpatterns = [

    url(r'home/',home, name='home'),
    url(r'get_stores',get_stores, name = 'store_details'),
    url(r'add_stores',add_stores,name = 'add_stores'),
    url(r'success',success,name='success'),

    url(r'delete/(?P<pid>[\d]+)/$', delete_store),
    url(r'update/(?P<pid>[\d]+)/$', store_update),

    url(r'get_products', GetProducts.as_view(), name='get_products'),
    url(r'add_products', AddProducts.as_view(), name='add_products'),



]