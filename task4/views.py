from django.shortcuts import render


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
    context = {
        'title': title,
        'products': products
    }
    return render(request, 'magazine.html', context)


def cart(request):
    title = 'Ваша Корзина'
    cart_info = 'Ваша корзина пуста'
    context = {
        'title': title,
        'cart_info': cart_info
               }
    return render(request, 'cart.html', context)
