from django.shortcuts import render
from django.shortcuts import get_object_or_404 , redirect
from django.views.decorators.http import require_POST

from products.models import Product
from .cart import Cart
from .forms import AddToCartForm

def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace' : True
        })

    return render(request , 'cart/cart_detail.html' ,{'cart' : cart})

@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=False)  # تغییر این خط

    return redirect('cart:cart_detail')



def remove_to_cart_view(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)

    cart.remove(product)
    return redirect('cart:cart_detail')



# def add_to_cart_view(request , product_id):
#     cart = Cart(request)
#
#     product = get_object_or_404(Product , id=product_id)
#     form = AddToCartForm(request.POST)
#
#     if form.is_valid():
#         cleaned_data = form.cleaned_data
#         quantity = cleaned_data['quantity']