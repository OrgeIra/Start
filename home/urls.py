from django.urls import path
from home import views

urlpatterns = [
    path('', views.category_list, name='index'),  
    path('categories/<int:pk>/products_list/', views.products_list, name='products_list'), 
]
