from django.urls import path
from .views import add_purchase_view, chart_select_view, sales_dist_view

app_name = 'products'

urlpatterns = [
    path('', chart_select_view, name='main-products-view'),
    path('add/', add_purchase_view, name='add-purchase-view'),
    path('sales/', sales_dist_view, name='sales-view')
    
]


