from django.shortcuts import render,redirect
from .forms import Register,LoginForm,AddProduct,CheckOutForm,UpdateProduct
from django.contrib.auth import login,logout,authenticate
from .models import ProductModel,CartModel,OrderHistoryModel,CustomerModel
from datetime import datetime
from django.contrib import messages

# Create your views here.

class ShoppingCart:
    
    def loginPage(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        forms=LoginForm()
        return render(request,'loginPage.html',{'forms':forms})
    
    def signIn(self,request):
        if request.method=='POST':
            usern = request.POST['username']
            passwd = request.POST['password']
            user = authenticate(username=usern,password=passwd)
            if user is not None:
                login(request,user)
                messages.success(request,f"Successfully {user} logged In")
                return redirect('home')
            else:
                return redirect('home')
        return redirect('home')
        

    def signUpPage(self,request):
        if request.method=='POST':
            forms=Register(request.POST)
            if forms.is_valid():
                forms.save()
            messages.success(request,"Registered Successfully")
            return redirect('home')
        forms=Register()
        return render(request,'signUp.html',{'forms':forms})
    
    def signOut(self,request):
        logout(request)
        messages.warning(request,"Logout Successfully")
        return redirect('login')
    
    def homePage(self,request):
        products = ProductModel.objects.all()
        context = {
            'products':products
        }
        return render(request,'homePage.html',context)
    
    def addProduct(self,request):
        forms=AddProduct()
        if request.method == 'POST':
            forms = AddProduct(request.POST,request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(request,"Successfully Added")
                return redirect('home')
                
            return redirect('addProduct')
        
        return render(request,'addProduct.html',{'forms':forms})
    
    def addToCart(self,request,id):
        product = ProductModel.objects.get(id=id)
        title = product.title
        price = product.price
        img = product.img
        
        data = CartModel(
            title = title,
            price = price,
            img = img,
        )
        data.save()
        messages.success(request,"Added to Cart")
        return redirect('home')
    
    def cart(self,request):
        product = CartModel.objects.all()
        total = 0
        for i in product:
            total = total + i.price
        
        data = {
            'product':product,
            'total':total
        }
            
        return render(request,'cart.html',data)
    
    def remove(self,request,id):
        data = CartModel.objects.get(id=id)
        data.delete()
        messages.success(request,"Registered Successfully")
        return redirect('cart')
    
    def checkOut(self,request):
        forms = CheckOutForm()
        if request.method == 'POST':
            forms = CheckOutForm(request.POST) 
            name = request.POST['name']
            if forms.is_valid():
                forms.save()
                
                current_time = datetime.now()
                dateAndTime = current_time.strftime("%Y-%m-%dT%H:%M:%S")  
                
                data = CartModel.objects.all()
                
                for i in data:
                    img = i.img
                    history = OrderHistoryModel(
                    name = name,
                    img = img,
                    dateAndTime = dateAndTime
                    )
                    history.save()
                
                data.delete()
                messages.success(request,"Ordered Placed Successfully")
                
                return redirect('home') 
            return redirect('checkOut')
        
        return render(request,'checkOut.html',{'forms':forms})
    
    
    def history(self,request):
        data = OrderHistoryModel.objects.all()
        return render(request,'history.html',{'data':data})
    
    def update(self,request,id):
        product = ProductModel.objects.get(id=id)
        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            price = request.POST['price']
            data = ProductModel(
                id=id,
                title=title,
                desc=desc,
                price=price,
            )   
            data.save()
            products = ProductModel.objects.all()
            context = {
                'products':products
            }
            return render(request ,'homePage.html',context)   
        
        return render(request,'update.html',{'product':product})
    
    def delete(self,request,id):
        product = ProductModel.objects.get(id=id)
        product.delete()
        products = ProductModel.objects.all()
        context = {
            'products':products
        }
        return render(request ,'homePage.html',context)
    
    def customers(self,request):
        data = CustomerModel.objects.all()
        return render(request,'customer.html',{'data':data})
        
        
        

s=ShoppingCart()