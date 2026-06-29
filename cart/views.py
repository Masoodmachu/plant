import razorpay
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from plant.models import Product,fertilizer
from cart.models import Cart,Order,Account,Orders,Payment
from cart.forms import PaymentForm


# Create your views here.

@login_required
def cartview(request):
    u=request.user
    total=0
    p=Cart.objects.filter(user=u)

    for i in p:
        total=total+i.quantity*i.product.price


    return render(request,"addtocart.html",{'c':p,'total':total})

# def addtocart(request,n):
#     p=Product.objects.get(id=n)
#     u=request.user
#     try:
#         cart=Cart.objects.filter(user=u,product=p)
#         if(p.stock>0):
#             cart.quantity+=1
#             cart.save()
#     except:
#         if (p.stock>0):
#             cart = Cart.objects.create(user=u,product=p,quantity=1)
#             cart.save()
#
#     return cartview(request)
@login_required
def addtocart(request,p):

    p=Product.objects.get(id=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(p.stock>0):
            cart.quantity+=1
            cart.save()
            p.stock-=1
            p.save()
    except:
        if (p.stock > 0):
            cart =Cart.objects.create(user=u,product=p,quantity=1)
            cart.save()
            p.stock -=1
            p.save()



    return cartview(request)

def removecart(request,p):
    p=Product.objects.get(id=p)
    u=request.user

    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
            p.stock+=1
            p.save()
        else:
            cart.delete()
            p.stock+=1
            p.save()
    except:
        cart = Cart.objects.create(user=u, product=p,quantity=1)
        cart.save()
        p.stock -= 1
        p.save()

    return cartview(request)

def deletecart(request,p):
    p=Product.objects.get(id=p)
    u=request.user

    try:
        cart=Cart.objects.get(user=u,product=p)
        cart.delete()
        p.stock+=cart.quantity
        p.save()
    except:
        pass
    return cartview(request)


# def orderform(request):
#     u=request.user
#     c=Cart.objects.filter(user=u)
#
#     if(request.method=='POST'):
#
#         phone=request.POST['phonenumber']
#         address=request.POST['address']
#         acc=request.POST['accountnumber']
#
#         total = 0
#         for i in c:
#             total=total+i.quantity*i.product.price
#
#         try:
#             acc=Account.objects.get(account_number=acc)
#             acc.save()
#
#             if(acc.amount>=total):
#                 o=Order.objects.create(user=u,product=i.product,phone=phone,address=address,item_count=i.quantity,order_status='paid')
#                 o.save()
#                 acc.amount=acc.amount-total
#                 acc.save()
#                 c.delete()
#
#                 msg="orederd successfully"
#                 return render(request,"order.html",{'message':msg})
#
#             else:
#                 msg="Inefficient Amount"
#                 return render(request,"order.html",{'message':msg})
#         except:
#             pass
#
#
#     return render(request,"orderform.html")



# def orderform(request):
#
#     u=request.user
#     c=Cart.objects.filter(user=u)
#
#
#     if(request.method=='POST'):
#
#         phone=request.POST['phone']
#         address=request.POST['address']
#         acc=request.POST['accountnumber']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email=request.POST['email']
#         house=request.POST['house']
#         postal_code=request.POST['postal_code']
#         city=request.POST['city']
#         message_to_seller=request.POST['message_to_seller']
#
#
#         total = 0
#         for i in c:
#             total=total+i.quantity*i.product.price
#
#             try:
#                 acc=Account.objects.get(account_number=acc)
#                 acc.save()
#
#                 if(acc.amount>=total):
#                     o=Orders.objects.create(user=u,product=i.product,phone=phone,address=address,item_count=i.quantity,first_name=first_name,last_name=last_name,email=email,city=city,house=house,postal_code=postal_code,message_to_seller=message_to_seller,order_status='paid')
#                     o.save()
#                     acc.amount=acc.amount-total
#                     acc.save()
#                     c.delete()
#
#                     msg="orederd successfully"
#                     return render(request,"order.html",{'message':msg})
#
#                 else:
#                     msg="Inefficient Amount"
#                     return render(request,"order.html",{'message':msg})
#             except:
#                 pass
#
#
#     return render(request,"dt.html",{'c':c})
#


def orderform(request):

    u=request.user
    c=Cart.objects.filter(user=u)


    if(request.method=='POST'):

        phone=request.POST['phone']
        address=request.POST['address']
        acc=request.POST['accountnumber']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        house=request.POST['house']
        postal_code=request.POST['postal_code']
        city=request.POST['city']
        message_to_seller=request.POST['message_to_seller']


        total = 0
        for i in c:
            total=int(total+i.quantity*i.product.offer_price)

            o=Orders.objects.create(user=u,product=i.product,phone=phone,address=address,item_count=i.quantity,first_name=first_name,last_name=last_name,email=email,city=city,house=house,postal_code=postal_code,message_to_seller=message_to_seller,order_status='paid')
            o.save()
            # return payments(request)
            client = razorpay.Client(auth=('rzp_test_63LXyFiiPBDdj6', 'fNSVxdIPrHOZYR293PVdevOF'))

            response_payment = client.order.create(dict(amount=total * 100, currency='INR'))

            order_id = response_payment['id']
            order_status = response_payment['status']

            if order_status == 'created':
                ord = Payment(name=first_name,
                              amount=total,
                              order_id=order_id,
                              )
                ord.save()

                response_payment['name'] = first_name
                return render(request, 'payment.html', {'payment': response_payment})

    return render(request,"dt.html",{'c':c})




# def payments(request):
#     u=request.user
#     total = 0
#     c = Cart.objects.filter(user=u)
#     for i in c:
#         total = total = total + i.quantity * i.product.offer_price
#
#     if (request.method == 'POST'):
#         name = request.POST['name']
#         amount = int(request.POST['amount'])
#
#         # create razorpay client
#
#         client = razorpay.Client(auth=('rzp_test_2EemDpSu9eqwId', '5hzNGWmuL2eNlstBDk6UdI5m'))
#
#         # create order
#
#         response_payment = client.order.create(dict(amount=amount * 100, currency='INR'))
#
#         order_id = response_payment['id']
#         order_status = response_payment['status']
#
#         if order_status == 'created':
#             payments = Payment(
#                 name=name,
#                 amount=amount,
#                 order_id=order_id
#             )
#             payments.save()
#             response_payment['name'] = name
#
#             form = paymentForm(request.POST or None)
#             return render(request, 'payment.html', {'form': form, 'payment':response_payment})
#
#     form = paymentForm()
#     return render(request, "payment.html", {'form': form,'total':total})
#
#
#
# def payment_status(request):
#     response=request.POST
#     params_dict={
#         'razorpay_order_id':response['razorpay_order_id'],
#         'razorpay_payment_id':response['razorpay_payment_id'],
#         'razorpay_signature':response['razorpay_signature']
#     }
#
#     #clientinstance
#
#     client=razorpay.Client(auth=('rzp_test_2EemDpSu9eqwId','5hzNGWmuL2eNlstBDk6UdI5m'))
#
#     try:
#          status=client.utility.verify_payment_signature(params_dict)
#          payments=Payment.objects.get(order_id=response['razorpay_order_id'])
#          payments.razorpay_payment_id=response['razorpay_payment_id']
#          payments.paid=True
#          print(payments)
#          payments.save()
#          return render(request,"payment_status.html",{'status':True})
#     except:
#         return render(request,'payment_status.html', {'status': False})
#

def payments(request):
    c=Cart.objects.all()
    amount=0
    for i in c:
        amount=amount+i.quantity*i.product.price

    if(request.method=="POST"):
        name=request.POST.get('name')
        # amount=int(request.POST.get('amount'))

        client=razorpay.Client(auth=('rzp_test_63LXyFiiPBDdj6','fNSVxdIPrHOZYR293PVdevOF'))

        response_payment=client.order.create(dict(amount=amount * 100,currency='INR'))

        order_id=response_payment['id']
        order_status=response_payment['status']

        if order_status=='created':
            ord=Payment(name=name,
                       amount=amount,
                       order_id=order_id,
                       )
            ord.save()

            response_payment['name']=name

            form=PaymentForm(request.POST or None)
            return render(request, 'payment.html', {'forms': form,'payment':response_payment})

    form = PaymentForm(request.POST or None)
    return render(request,'payment.html',{'forms':form})
@csrf_exempt
def payment_status(request):
    if request.method == "POST":
        # Handle the Razorpay response here.
        response = request.POST
        payment_id = response.get('razorpay_payment_id')
        order_id = response.get('razorpay_order_id')
        signature= response.get('razorpay_signature')
    param_dict={
        'razorpay_order_id': order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }
    client = razorpay.Client(auth=('rzp_test_63LXyFiiPBDdj6', 'fNSVxdIPrHOZYR293PVdevOF'))

    try:

        client.utility.verify_payment_signature(param_dict)

        ord=Payment.objects.get(order_id=response['razorpay_order_id'])
        ord.razorpay_id=response['razorpay_payment_id']
        ord.paid=True
        ord.save()
        return render(request,'payment_success.html',{'status':True})

    except:

        return render(request, 'payment_success.html', {'status': False})

    return render(request,'payment_success.html')




@login_required()
def orderview(request):
    u=request.user
    o=Orders.objects.filter(user=u)

    return render(request,"orderview.html",{'o':o,'u':u})



# @login_required
# def addtocart(request,p):
#
#     p=fertilizer.objects.get(id=p)
#     u=request.user
#     try:
#         cart=Cart.objects.get(user=u,product=p)
#         if(p.stock>0):
#             cart.quantity+=1
#             cart.save()
#             p.stock-=1
#             p.save()
#     except:
#         if (p.stock > 0):
#             cart =Cart.objects.create(user=u,product=p,quantity=1)
#             cart.save()
#             p.stock -=1
#             p.save()
#
#
#
#     return cartview(request)

def det(request):
    return render(request,"dt.html")



