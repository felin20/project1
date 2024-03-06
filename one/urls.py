from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path



urlpatterns=[
    path('list',views.list,name='list'),
    path('det/<int:id>',views.det,name='det'),
    path('category/men',views.men,name='men'),
    path('category/women',views.women,name='women'),
    path('category/jewelery',views.jewelery,name='jewelery'),
    path('category/electronics',views.electronics,name='electronics')
    
    ]