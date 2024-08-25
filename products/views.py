from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,carty,remove,check
from django.db.models.functions import Cast
from django.db.models import Sum, F

from .forms import searchForm,cartForm,removeForm,checkForm
def index(request):
    products= Product.objects.all()
    return render(request,'index.html',{'products':products})


def cart(request):
    if request.method=="POST":
        formy=cartForm(request.POST)
        if formy.is_valid():
            name=formy.cleaned_data['name']
            q=Product.objects.get(name=name)

            z=carty.objects.create(name=q.name,stock=q.stock,price=q.price,image_url=q.image_url)
        return redirect('cart')
    cart_items=carty.objects.all()
    cart_item_count=cart_items.count()
    #ammount=carty.objects.aggregate(total=sum('price'))['total']
    return render(request, 'cart.html', {'cart_items': cart_items,'count':cart_item_count,})#'ammount':ammount})
def search(request):
    if request.method=="POST":
        form=searchForm(request.POST)
        if form.is_valid():
            search_name=form.cleaned_data['search_name']
            p=Product.objects.get(name=search_name)
            return render(request,'search.html',{'data':p})
        else:
            form=searchForm()
    return render(request, 'search.html', {'form': form})
def product_detail(request,id):
    product=Product.objects.get(id=id)

    return render(request,'product_detail.html',{'product':product})
def checkout(request):
    return render(request,'checkout.html')
def remove(request):
    if request.method=="POST":
        form=removeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            p=carty.objects.filter(name=name)
            p.delete()
            return render(request,'remove.html')
        else:
            form=removeForm()
    return render(request,'cart.html',{'form':form})
def checky(request):
    if request.method=="POST":
        check_form=checkForm(request.POST)
        if check_form.is_valid():
            name=check_form.cleaned_data['name']
            phone_number=check_form.cleaned_data['phone_number']
            address=check_form.cleaned_data['address']
            mail=check_form.cleaned_data['mail']
            q=check(name=name,mail=mail,phone_number=phone_number,address=address)
            q.save()
            z = carty.objects.aggregate(total_price=Sum('price'))['total_price']

            cart_items=carty.objects.all()
            cart_item_count=cart_items.count()
            return render(request,'next.html',{'price':z,'count':cart_item_count})
    else:
        check_form=checkForm()
    return render(request,'checkout.html',{'check_form':check_form})
