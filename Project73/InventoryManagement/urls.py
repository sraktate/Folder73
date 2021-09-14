from django.urls import path
from . import views

urlpatterns =[
    path('add-product/', views.addProduct, name='addproduct'),
    path('ho/',views.homeView,name='home'),
    path('p-list/', views.productListView,name='p-list'),
    path('update-p-list/<int:id>',views.updateProduct , name='updateList'),
    path('delete-p-list/<int:id>',views.deleteProductDetails , name='deleteList')
]