from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
def index(request):
   
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products,}
    # allProds=[[products,range(1,nSlides),nSlides],
    #           [products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def login(request):
    return render(request,'shop/log_in.html')
def signup(request):
    return render(request,'shop/sign_up.html')
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phn=request.POST.get('phn','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phn,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')
def search(request):
    return render(request,'shop/search.html')
def productView(request, myid):
    #Fetch the product using the id
    # sending it as a list
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html",{'product':product[0]})
def checkout(request):
    return render(request,'shop/checkout.html')


# for login and signup


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/log_in.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = UserCreationForm()
    return render(request, 'shop/sign_up.html', {'form': form})
