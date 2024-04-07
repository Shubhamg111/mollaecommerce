from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("contact",views.contact,name='contact'),
    path('products',views.product_list, name="productlist"), 
    path('productview/<slug>', views.productview, name="productview"),
    path('product-category/<slug>',views.productcategory,name="product_category"),
    path('search',views.productsearch,name='search'),

    
]