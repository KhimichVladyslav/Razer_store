from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product, Order, OrderItem
from .basket import Basket
from .forms import CartAddProductForm
from django.contrib import messages

import random


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                   quantity=cd['quantity'],
                   update_quantity=cd['update'])
    return redirect('basket:basket_detail')


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.delete(product)
    return redirect('basket:basket_detail')


def basket_detail(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})

    return render(request, 'store/basket/basket_detail.html', {'basket': basket})


def checkout(request):
    return render(request, 'store/basket/checkout.html')


@require_POST
def placeorder(request):
    # if request.method == 'POST':

    """база окремого замовлення"""
    neworder = Order()
    neworder.first_name = request.POST.get('first_name')
    neworder.last_name = request.POST.get('last_name')
    neworder.email = request.POST.get('email')
    neworder.phone = request.POST.get('phone')
    neworder.address = request.POST.get('address')
    neworder.city = request.POST.get('city')
    neworder.zipcode = request.POST.get('zipcode')

    basket = Basket(request)
    neworder.total_price = basket.get_total_price()

    """рандомно створюємо номер замовлення"""
    track_no = 'razer_' + str(random.randint(1111, 9999))
    while Order.objects.filter(tracking_no=track_no) is None:
        track_no = 'razer_' + str(random.randint(1111, 9999))
    neworder.tracking_no = track_no

    neworder.save()

    """база всіх товарів в КОНКРЕТНОМУ замовленні"""
    for item in basket:
        OrderItem.objects.create(
            order=neworder,
            product=item['product'],
            price=item['product'].price,
            quantity=item['quantity'],
        )

    basket.clear()

    messages.success(
        request,
        f'{neworder.first_name}, your order "{track_no}" '
        f'has been placed successfully, wait for the operator to call you.')

    return render(request, 'store/home.html')

    # return redirect('/')
