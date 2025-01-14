from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from dhapp.models import Product,CustomerOrder,Feedback,Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse

# Create your views here.


def admin_login(request):
    try:

        if request.method == 'POST':               
            username = request.POST['username']
            password = request.POST['password']

            admin_Login = User.objects.filter(username = username) 
                
            
            if not admin_Login.exists():
                messages.info(request, 'Contact to admin')
                return redirect('admin_login')
            
            admin_Login=authenticate(username=username,password=password)
            if admin_Login.is_superuser==True and admin_Login.is_staff==True:
                login(request,admin_Login)
                return redirect('dashboard')
            
            messages.info(request, 'Please contact to admin')
            return redirect('admin_login')
        
    except:
        messages.info(request,'You Are not authorize to visit this page..')
        return redirect('admin_login')
    
    return render(request, 'admin-signin.html')

@login_required(login_url='admin_login')
def dashboard(request):
    
    return render(request, 'dashboard.html')

def signout(request):
    logout(request)
    return redirect('admin_login')

@login_required(login_url='admin_login')
class Products:
    def product(request):
        pdt = Product.objects.all()
        return render(request, 'product.html',{'pdt':pdt})

@login_required(login_url='admin_login')  
class Add_Product:
    def add_product(request):
        if request.method == 'POST' and request.FILES:
            img = request.FILES['product-image']
            product_titles = request.POST['product-title']
            product_price = request.POST['product-price']
            descriptions = request.POST['description']
            delivery_charges = request.POST['delivery-charge']
            save_product = Product(image = img, product_name = product_titles, price=product_price, description=descriptions, delivery_charge=delivery_charges )
            save_product.save()
            return redirect('product')


        Categorys= Category.objects.all()
        context={
            'Categorys':Categorys,
        }
        return render(request, 'addproduct.html',context)
    
class Order:
    def order_list(request):
        Od_lst = CustomerOrder.objects.all()
        contax = {
            'Od_lst':Od_lst
        }
        return render(request, 'Order.html',contax)

def delete_Orders(reqeust,id):
    dl = CustomerOrder.objects.get(id=id)
    dl.delete()
    return redirect('Order_list')

def FeedBack(request):
    feedback =  Feedback.objects.all()
    contax = {
        'feedback':feedback,
    }
    return render(request, 'feedBack.html',contax)

def delete_products(request,id):
    get_del_product = Product.objects.get(id=id)
    get_del_product.delete()
    return redirect('product')

def Edit_Product(request,id):
    if request.method =='POST' and request.FILES:    
        show_product = Product.objects.get(id=id)

        show_product.image = request.FILES['product-image']
        show_product.product_name = request.POST['product-title']
        show_product.price = request.POST['product-price']
        show_product.description = request.POST['description']
        show_product.delivery_charge = request.POST['delivery-charge']
        show_product.save()
        return redirect('product')


    show_product = Product.objects.get(id=id)
    context = {
        'show_Product':show_product
    }
    return render(request, 'edit_product.html',context)

def manage_profile(request):
    return render(request, 'manage/account_manager.html')

def Password_change(request):
    try:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, 'Password is change successfully')
                return redirect('dashboard')

            
            messages.error(request, 'Re-enter or Check the password correctly')
            return redirect('password_change')    
        else:  
            fm = PasswordChangeForm(user=request.user)
    except:
        return HttpResponse('Please check Internet')
    return render(request, 'change_password.html',{'fm':fm})