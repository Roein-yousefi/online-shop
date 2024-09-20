from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _

class Cart:
    def __init__(self , request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product , quantity=1 , replace_current_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id]= {'quantity':quantity}
        else:
            # اگر مقدار جدید را جایگزین کنیم
            if replace_current_quantity:
                self.cart[product_id]['quantity'] = quantity  # مقدار جدید را جایگزین می‌کند
            else:
                self.cart[product_id]['quantity'] = quantity  # مقدار جدید را به جای مقدار قبلی قرار می‌دهد

        messages.success(self.request, _('product added'))

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request , _('product remove'))
            self.save()

    def save(self):
        self.session.modified = True



    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear_all(self):
        del self.session['cart']
        self.save()

    def get_total(self):
        product_ids = self.cart.keys()


        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())


    # def __iter__(self):
    #     product_ids = self.cart.keys()
    #
    #     products = Product.objects.filter(id__in=product_ids)
    #
    #     cart = self.cart.copy()
    #     for product in products:
    #         cart[str(product.id)]['product_obj'] = product














# class Cart:
#     def __init__(self , request):
#         self.request = request
#         self.session = request.session
#         cart = self.session.get('cart')
#
#         if not cart:
#             self.session['cart'] = {}
#             cart = self.session['cart']
#
#         self.cart = cart