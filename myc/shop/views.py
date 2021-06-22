from django.http import HttpResponse
from django.shortcuts import render
from math import ceil
from .models import Product,Contact,Orders,Orderupdate
import json

def index(request):
    # product = Product.objects.all()
    # n= len(product)
    # slides_no = n//4 + ceil(n/4 - n//4)
    # print(slides_no)
    # allProduct = [[product, range(1, slides_no), slides_no],
    #               [product, range(1, slides_no), slides_no]]
    # Dictionary = {'no_slides': slides_no,'product':products,'range': range(1,slides_no)}
    allProduct = []
    cat_of_product = Product.objects.values('category', 'id') # we are storing the category and product_id of product in  Category Variable
    category_set = {item['category'] for item in cat_of_product} # set comprehension created  here like list comprehension
    for cat in category_set:
        product = Product.objects.filter(category=cat)
        n = len(product)
        slides_no = n//4 + ceil(n/4 - n//4)
        allProduct.append([product, range(1, slides_no), slides_no])
    Dictionary = {'allproduct': allProduct}
    # Dictionary = {'no_slides': slides_no,'product':products,'range': range(1,slides_no)}
    return render(request, "shop/index.html", Dictionary)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone= request.POST.get('phone','')
        Query = request.POST.get('Query', '')
        info = Contact(name = name,email= email,phone=phone,Query=Query ) # save the data in to database by using contact Class
        info.save() 
        thank = True
        return render(request, "shop/contact.html",{'thankyou':thank})
    return render(request, "shop/contact.html")

def tracker(request):
    if request.method =='POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email','')
        # print(orderId)
        # print(email)
        print(Orders.order_id) 
        try:
            order = Orders.objects.filter(order_id= request.POST.get('orderId'), email= request.POST.get('email'))
            # order1= Orders.objects.all()
            if len(order)>0:
                update = Orderupdate.objects.filter(order_id=orderId)
                # print(update)
                updates =[]
                for item in update:
                    updates.append({'text': item.upadate_desc, 'time': item.timestamp})
                    response= json.dumps([updates,order[0].ItemJson],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,"shop/tracker.html")


def proview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request, "shop/proview.html",{'product':product[0]})


def checkout(request):
    if request.method == "POST":
        ItemJson = request.POST.get('ItemJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address= request.POST.get('address','')
        address_line_2= request.POST.get('address_line_2','')
        state = request.POST.get('state','')
        city= request.POST.get('city','')
        zip_code= request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        info = Orders(ItemJson= ItemJson, name = name,email= email,address=address,address_line_2=address_line_2,
        state= state, city = city,zip_code = zip_code,phone=phone ) # save the data in to database by using contact Class
        info.save()
        thank = True
        Id = info.order_id
        print(Id)
        update = Orderupdate(order_id=info.order_id,upadate_desc= "The order has been placed")
        update.save()
        return render(request, "shop/checkout.html",{'thank':thank,'Id':Id})
    return render(request, "shop/checkout.html")


def search(request):
    return render(request, "shop/search.html")
