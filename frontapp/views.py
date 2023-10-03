from django.shortcuts import render
import requests

def home(request):
    categories = get_all_categories()
    products =get_all_products()
    context = {'categories': categories, 'products':products}
    return render(request, 'frontapp/home.html', context)

def get_all_categories():
    end_point = 'http://localhost/api/category/'
    response = requests.get(end_point)
    return response.json()

def get_all_products():
    end_point = 'http://localhost/api/product/'
    response = requests.get(end_point)
    return response.json()
