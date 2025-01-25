from django.shortcuts import render,redirect
from django.http import HttpResponse
from appMM.models import Logintable,signuptable,Producttable,Carttable,Billtable
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

#homepage after login
def home(request):
    return render(request,"home.html")

#gallery
def gallery_view(request):
    return render(request,"gallery.html")

#about us
def our_story(request):
    return render(request,"our_story.html")

#landing page
def landing_page(request):
    return render(request,"landing_page.html")

#user signup/registration
def sign_up(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]
        x = Logintable(Username=f, Password=g, Type="User")
        x.save()
        q = signuptable(Loginid=x, firstname=a, lastname=b, place=c, mobile=d, email=e, Username=f, Password=g, Type="User")
        q.save()
        return render(request, "signup_http.html")  # Render success page
    return render(request, "signup.html")

#user login
def log_in(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        try:
            q = signuptable.objects.get(Username=a)
            if q.Password == b:
                request.session["member_id"] = q.id
                return render(request, "home.html")
            else:
                return HttpResponse("Incorrect Password")
        except signuptable.DoesNotExist:
            return render(request, "login_http.html")

    return render(request, "login.html")


#workshop info page
def workshop_view(request):
    return render(request,"workshop.html")

#login fail redirect page
def log_http(request):
    return render(request,"login_http.html")

def signup_http(request):
    return render(request,"signup_http.html")
#menu
def menu_view(request):
    return render(request,"menu.html")

#library
def books(request):
    return render(request,"books.html")

#course detail page
def barista_view(request):
    return render(request,"barista.html")

#product registration page
def productregistration(request):
    if request.method == "POST":
        a = request.POST["name1"]
        d = request.FILES["name4"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        q = Producttable(Productname=a, Quantity=b, Unitprice=c, Image=d)
        q.save()
        return HttpResponse("Product added")
    return render(request, "productregistration.html")

#product data
def allproductprofiledata(request):
    q = Producttable.objects.all()
    return render(request, "productalldata.html", {"allproductkey": q})

#update
def productprofileupdate(request, id3):
    q = Producttable.objects.get(id=id3)
    if request.method == "POST":
        q.Productname = request.POST["name1"]
        q.Image = request.FILES["name4"]
        q.Quantity = request.POST["name2"]
        q.Unitprice = request.POST["name3"]
        q.save()
        return HttpResponse("Update Success")

    return render(request, "productprofile.html", {"productprofilekey": q})

#delete
def productdelete(request, id2):
    q = Producttable.objects.get(id=id2)
    q.delete()
    return HttpResponse("Product is deleted")

#shop
def userproductdata(request):
    q = Producttable.objects.all()
    return render(request, "userproductdata.html", {"userproductdatakey": q})

#shop product detail
def data(request, id):
    a = Producttable.objects.filter(id=id).first()
    return render(request, "datapage.html", {"detailskey": a})

#cart success
def usercart(request, id4, id5, id):
    Pid = id4
    Pname = id5
    Price = id

    if request.method == "POST":
        c = request.POST["name3"]
        total = int(c) * int(Price)
        q = Carttable(Productid=Pid, Productname=Pname, Quantity=c, price=total, Userid=request.session["member_id"])
        q.save()
        a = Billtable(Productid=Pid, Productname=Pname, Quantity=c, price=total, Userid=request.session["member_id"],
                      Date=datetime.date.today())
        a.save()

        return render(request, "cartsuccess.html")

    return render(request, "cart.html")

#cart details
def usercartdata(request):
    a = Carttable.objects.filter(Userid=request.session["member_id"])
    x=0
    if a:
        for i in a:
            p=i.price
            x=x+p
            pid=i.Productid
            q=i.Quantity
            c=i.id

        return render(request, "usercartdata.html",{"usercartdatakey":a,"sum":x,"Productid":pid,"Quantity":q,"id":c})
    else:
        return HttpResponse("Cart is empty")

#delete item from cart
def usercartdelete(request,id10):
    q=Carttable.objects.get(id=id10)
    q.delete()
    return HttpResponse("Item  deleted from the cart")

#bill
def userbilldata(request):
    a = Billtable.objects.filter(Userid=request.session["member_id"])
    x=0
    if a:
        for i in a:
            p=i.price
            x=x+p
            pid=i.Productid
            q=i.Quantity
            c=i.id
            n=i.Firstname


        return render(request, "userbilldata.html",{"usercartdatakey":a,"sum":x,"Productid":pid,"Quantity":q,"id":c,"Date":datetime.date.today(),"Firstname":n})
    else:
         return HttpResponse("No orders")

#bill
def userbill(request):
    return render(request, "userbilldata.html")

#pay
def userpayment(request):
    a = Carttable.objects.filter(Userid=request.session["member_id"])
    x = 0
    for i in a:
        p = i.price
        x = x + p

    return render(request,"userpayment.html",{"sum":x,"id_new":request.session["member_id"]})

#pay success
def userpaymentsuccess(request):
        cart = Carttable.objects.all()
        for i in cart:
            product = Producttable.objects.filter(Productname=i.Productname)
            if product:
                for j in product:
                    q = j.Quantity
                    Producttable.objects.filter(Productname=j.Productname).update(Quantity=q - i.Quantity)
        bill = Carttable.objects.all()
        for i in bill:
            a = Producttable.objects.filter(Productname=i.Productname).update()
            # print(a)
        Carttable.objects.filter(Userid=request.session["member_id"]).delete()
        return render(request, "lastpage.html")


#search bar
def userproductsearch(request):
    if request.method=="POST":
        a=request.POST["name1"]
        q=Producttable.objects.filter(Q(Productname__icontains=a))
        if not q:
            return HttpResponse("no search result")
    return render(request,"userproductdata.html",{"usersearchkey":q})

