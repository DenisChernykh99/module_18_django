from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def main(request):
    return render(request, 'main.html')


def magazine(request):
    products = [
        'Air Jordan', 'Dunk Low Retro', ''
    ]
    return render(request, 'magazine.html')


def cart(request):
    return render(request, 'cart.html')
