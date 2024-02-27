from django.urls import path
from . import views

app_name='e_commerce_app'

urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetail,name='product_category_detail'),
]