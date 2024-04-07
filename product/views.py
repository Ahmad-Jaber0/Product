from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import requests
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login,logout
from .serializers import *
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404


# /products ---> index .   so we need mapping , go to urls
def index(request):
    x=Product.objects.all()
    return render(request,'index.html',{'pro':x})

class AddProductAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_product.html'
    def get(self, request):
        form = ProductForm()
        return Response({'form': form}, template_name='add_product.html')

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditProductAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'edit_product.html'
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        form = ProductForm(instance=product)
        return Response({'form': form, 'pk': product.pk}, template_name='edit_product.html')

    def post(self, request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteProductAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'delete_product.html'
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    

    def get(self, request, pk):
        product = self.get_object(pk)
        form = ProductForm(instance=product)
        return Response({'form': form, 'product': product}, template_name='delete_product.html')    

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return JsonResponse({},status=status.HTTP_204_NO_CONTENT)    
    
'''
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



def no_rest_from_model(request):
    data = Product.objects.all()
    #data1 = [i for i in data.values()]
    response = {
        'Product': list(data.values())
    }
    return JsonResponse(response)


class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, pk):
        return self.retrieve(request)
    def put(self, request, pk):
        return self.update(request)
    def delete(self, request, pk):
        return self.destroy(request)


class generics_list(generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class generics_pk(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class viewsets_Product(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


def fahrenheit_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * (5.0/9.0) 
    
    return celsius

def wether(request):
    api_url = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city_name="Nablus"
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
    '''