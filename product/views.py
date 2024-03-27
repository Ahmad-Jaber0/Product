from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import requests
from django.http.response import JsonResponse

def no_rest_from_model(request):
    data = Product.objects.all()
    response = {
        'Product': list(data.values())
    }
    return JsonResponse(response)

def fahrenheit_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * (5.0/9.0) 
    
    return celsius

def wether(request):
    api_url = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city_name="palestine"
    url=api_url+city_name
    response=requests.get(url)
    content=response.json()
    city_weather = {
                'city': city_name,
                'temperature': fahrenheit_to_celsius(content['main']['temp']),
                'description': content['weather'][0]['description'],
                'icon': content['weather'][0]['icon'],
            }
    return render(request,"wether.html",city_weather)





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