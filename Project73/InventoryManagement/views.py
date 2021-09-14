
from django.shortcuts import redirect, render
from .forms import ProductFormModel
from.models import Product
# Create your views here.


def addProduct(request):
    form = ProductFormModel()
    if request.method == 'POST':
        form = ProductFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('p-list')
    template_name ='Inven_app/RegisterProduct.html'
    context = {'form':form}
    return render(request,template_name,context)

def homeView(request):
    template_name = "Inven_app/Home.html"
    context ={}
    return render(request,template_name,context)

def productListView(request):
    template_name = "Inven_app/List_product.html"
    p_list = Product.objects.all()
    context ={'p_list':p_list}
    return render(request,template_name,context)

def updateProduct(request,id):
    p_list = Product.objects.get(id=id)
    form = ProductFormModel(instance=p_list)
    if request.method == 'POST':
        form = ProductFormModel(request.POST, instance=p_list)
        if form.is_valid():
            form.save()
            return redirect('p-list')
    template_name = "Inven_app/RegisterProduct.html"
    context = {'form':form}
    return render(request,template_name,context)

def deleteProductDetails(request,id):
    p_list = Product.objects.get(id=id)
    p_list.delete()
    return redirect('p-list')
