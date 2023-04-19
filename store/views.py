from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from basket.forms import CartAddProductForm
from .models import Category, Product


def home(request):
    return render(request, 'store/home.html')


def all_products(request):
    products = Product.products.order_by('?')[:]
    return render(request, 'store/all_products.html', {'products': products})


@login_required(login_url='/users/login/')
def all_products_by_price_min(request):
    products = Product.products.order_by('price')
    return render(request, 'store/all_products.html', {'products': products})


def all_products_by_price_max(request):
    products = Product.products.order_by('-price')
    return render(request, 'store/all_products.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


# отримує назву товару та перенаправляє нас до нового URL з описом КОНКРЕТНОГО товару
def product_detail(request, slug):
    # в product передається конкретний товар і вже по цьому в single.html виводиться інфа
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    basket_product_form = CartAddProductForm()
    return render(request, 'store/products/single.html',
                  {'product': product,
                   'basket_product_form': basket_product_form,
                   })



@require_GET
def search(request):
    query = request.GET.get('query')

    if query:
        price = Product.objects.filter(price__icontains=query)
        category = Category.objects.filter(name__icontains=query)
        title = Product.objects.filter(title__icontains=query)
        if price:
            return render(request, 'store/search.html', {'products': price, 'query': query})
        elif category:
            # тут по факту я просто розпаковую категорію (цикл складається з 1 ітерації)
            for item in category:
                all_filtered = Product.objects.filter(category=item)
                return render(request, 'store/search.html', {'products': all_filtered, 'query': query})
        elif title:
            return render(request, 'store/search.html', {'products': title, 'query': query})
        else:
            return render(request, 'store/search.html', {'query': query})
    else:
        messages.success(request, "Please enter some value, like... 'mice', 'razer', etc.")
        return render(request, 'store/search.html')
