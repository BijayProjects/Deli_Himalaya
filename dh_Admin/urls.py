from django.urls import path
from . import views
from dhapp.models import Product, Category, Customer, CustomerOrder, Feedback
urlpatterns=[
    path("",views.admin_login,name='admin_login'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path('LogOut/',views.signout,name='lgOut'),
    path('product/',views.Products.product, name='product'),
    path('+addPro/',views.Add_Product.add_product,name='addpd'),
    path('Order/',views.Order.order_list, name='Order_list'),
    path('Del-Orders/<int:id>',views.delete_Orders,name='dl_order'),
    path('feedBacks/',views.FeedBack,name='feedBack'),
    path('delete_products/id=<int:id>',views.delete_products,name='product_delete'),
    path('editproducts/<int:id>',views.Edit_Product, name='edit_products'),
    path('account_profile/',views.manage_profile,name='m_profile'),
    path('change_password/', views.Password_change,name='change-password'),
    
    # Django Admin Integration
    path('custom-admin/products/', views.CustomAdminView.as_view(model=Product), name='custom_admin_products'),
    path('custom-admin/categories/', views.CustomAdminView.as_view(model=Category), name='custom_admin_categories'),
    path('custom-admin/customers/', views.CustomAdminView.as_view(model=Customer), name='custom_admin_customers'),
    path('custom-admin/orders/', views.CustomAdminView.as_view(model=CustomerOrder), name='custom_admin_orders'),
    path('custom-admin/feedback/', views.CustomAdminView.as_view(model=Feedback), name='custom_admin_feedback'),
]