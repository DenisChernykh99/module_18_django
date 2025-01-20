from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def main(request):
    title = 'Главная'
    context = {'title': title}
    return render(request, 'main.html', context)


def magazine(request):
    title = 'Наш Магазин'
    products = [
        'Air Jordan', 'Dunk Low Retro', 'Adidas Super-Star II'
    ]
    return render(request, 'magazine.html', {'products': products, 'title': title})


def cart(request):
    title = 'Ваша корзина пуста'
    context = {'title': title}
    return render(request, 'cart.html', context)