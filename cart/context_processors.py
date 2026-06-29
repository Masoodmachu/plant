
from cart.models import Cart


def Total(request):
    count=0
    total = 0
    discount=0
    price=0

    if request.user.is_authenticated:
        u=request.user

        try:
            cart=Cart.objects.filter(user=u)
            for i in cart:
                count=count+i.quantity
                total = total + i.quantity * i.product.offer_price
                discount=discount+i.quantity*i.product.price-i.quantity*i.product.offer_price
                price=price+i.quantity*i.product.price
        except:
            count=0

    return {'count':count,'totalamount':total,'discount':discount,'price':price}


# def totalamount(request):
#     u = request.user
#     c = Cart.objects.filter(user=u)
#
#     total = 0
#     for i in c:
#         total = total + i.quantity * i.product.price

    # return {'totalamount':total}
