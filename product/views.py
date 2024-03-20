from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


# /products ---> index .   so we need mapping , go to urls
def index(request):
    x=Product.objects.all()
    return render(request,'index.html',{'pro':x})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')  
    return render(request, 'delete_product.html', {'product': product})