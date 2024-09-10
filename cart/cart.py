from products.models import Product

class Cart:
    def __init__(self , request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product , quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id]= {'quantity':quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
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
            yield item


    def __len__(self):
        return len(self.cart.keys())

    def clear_all(self):
        del self.session['cart']
        self.save()

    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(product.price for product in products)


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