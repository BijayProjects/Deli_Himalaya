from django.urls import path
from .import views

urlpatterns =[
    path('',views.Home.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('signup/',views.Signup.signup, name='signup'),
    path('signin/',views.SignIn.signin,name='signin'),
    path('signout/',views.Signout.signout,name='signout'),
    path('about/',views.About.about,name='about'),    
    path('search/',views.Search.search,name='search'),
    path('contact/',views.Contact.contact,name='contact'),
    path('base/',views.base_date,name='base_date'),
    path('order/<int:id>',views.Order.orderPurchase,name='order'),
    path('OrderSuccess/',views.success,name='orderSuccess'),
    path('showcategoy=<int:id>',views.ShowCategory,name='showcategory'),
]