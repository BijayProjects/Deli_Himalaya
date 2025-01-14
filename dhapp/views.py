from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Category,Product,CustomerOrder,Feedback
import datetime


from django.core.mail import send_mail

# Create your views here.
def base_date(request):
    ddd = datetime.datetime.now()
    
    return render(request, 'main/base.html',{'ddd':ddd})


class Home:
    def home(request):
        if request.method =='POST':
            fullname = request.POST['fullname']
            email =request.POST['email']
            comment = request.POST['comment']
            smg = Feedback(fullname=fullname,email=email,message=comment)
            smg.save()
            messages.success(request, 'Thank You For your Feedback, Stay connected and Have a Good Day..')
            return redirect('home')


        ddd = datetime.datetime.now()
        return render(request, 'main/home.html',{'ddd':ddd})


def menu(request):

    ddd = datetime.datetime.now()
    product = Product.objects.all()
    category = Category.objects.all()

    return render(request, 'main/menu.html',{'category':category,'product':product,'ddd':ddd})

class Signup:
    def signup(request):
        if request.method == 'POST':
            username = request.POST['username']
            email= request.POST['email']
            password = request.POST['password']
            confirm_password  =request.POST['confirm-password']


            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'User Already exit!')
                    return redirect('signup')
               
                elif User.objects.filter(email=email).exists():
                   messages.info(request, 'Email Already exit!')
                   return redirect('signup')
                else:
                    user = User.objects.create_user(username=username,email=email, password=password)
                    user.is_staff=False
                    user.is_superuser=False
                    user.save()
                    return redirect('signin')
            else:
                messages.info(request, 'Password did not match**')
                return redirect('signup')
            
        ddd = datetime.datetime.now()
        return render(request, 'main/signup.html',{'ddd':ddd})

class SignIn:
    def signin(request):
        if request.method =='POST':
            username = request.POST['email']
            password = request.POST['password']

            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid username')
                return redirect('signin')
            
            
            Usr=authenticate(username=username, password=password)
            if Usr is not None and Usr.is_active==False and Usr.is_staff==False:
                login(request,Usr)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Password')
    
        ddd = datetime.datetime.now()
        return render(request, 'main/signin.html',{'ddd':ddd})
class Signout:
    def signout(request):
        logout(request)
        return redirect('signin')
        # return render(request, 'main/chard.html',{'sv':sv})

class About:
    def about(request):
        ddd = datetime.datetime.now()
        return render(request, 'main/about.html',{'ddd':ddd})

class Search:
    def search(request):
        if request.method=='POST':
            search = request.POST['search']
            match = Product.objects.filter(product_name__contains=search)
            
            return render(request, 'main/search.html',{'match':match,'search':search})
        ddd = datetime.datetime.now()
        return render(request, 'main/search.html',{'ddd':ddd})
    
class Contact:
    def contact(request):
        ddd = datetime.datetime.now()
        return render(request, 'main/contact.html',{'ddd':ddd})
    
# Orer purchase


class Order:
    def orderPurchase(request,id):
        if request.method=='POST':
            product = Product.objects.get(id=id)

            CustomerName = request.POST['fullname']
            phoneNumber= request.POST['phoneNo']
            email = request.POST['email']
            city = request.POST['city']
            region = request.POST['region']
            street_address = request.POST['street-address']
            zip_code = request.POST['zip-code']
            quantitys = request.POST['quantitys']
            total_price = request.POST['total_price']

            product_name = product.product_name
            product_price = product.price
            subtotal = product.price
            order_total = total_price

            customeOrder=CustomerOrder(customerName = CustomerName, phoneNumber=phoneNumber,email=email,city=city,region=region,street_address=street_address,zip_code=zip_code,product_name=product_name,product_price=product_price,total=order_total, quantity=quantitys)
            customeOrder.save()
            messages.info(request,' Order is Successful')
            
            

            # email sending
            subject = 'Deli Himalaya'
            message = f'''Thank you for Your order You will receive your order under four hours it depend on your location!\n Your order is:\n Product Name: {product_name}, \n Total:Rs.{order_total}'''
            from_email = 'bijay2310tamang@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('orderSuccess')
        
            


        ord = Product.objects.get(id=id)
        price = ord.price
        delivery_charge = ord.delivery_charge

        total = price + delivery_charge
        ddd = datetime.datetime.now()
        return render(request, 'orders/order.html',{'ddd':ddd,'ord':ord,'total':total})
def success(request):
    return render(request, 'main/orderSuccess.html')

def ShowCategory(request,id):

    product = Product.objects.filter(category_id=id)
    category = Category.objects.all()

    return render(request, 'main/ShowCategory.html',{'item':product,'category':category})
