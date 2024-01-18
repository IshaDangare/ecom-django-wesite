from django.shortcuts import render
from .models import Product
    
# Create your views here.
def index(request):
    return render(request, 'index.html')
def product(request):
    allproducts = Product.objects.all()
    context = {'allproducts':allproducts}
    return render(request, 'index.html',context)
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")