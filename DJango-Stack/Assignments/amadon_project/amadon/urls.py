from django.urls import path
from . import views

app_name = 'amadon'

urlpatterns = [
    path('', views.product_list, name='product_list'),   # shop / homepage
    path('buy/', views.buy, name='buy'),                 # POST endpoint (will redirect)
    path('checkout/', views.checkout, name='checkout'),  # thank-you / totals page (GET)
]