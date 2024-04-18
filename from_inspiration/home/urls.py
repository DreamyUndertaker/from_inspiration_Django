from django.template.context_processors import static
from django.urls import path

from from_inspiration import settings
from home.views import ProductsList, CardDetailView

urlpatterns = [
    path('<slug:category_slug>/', ProductsList.as_view(), name='category_products_list'),
    path('', ProductsList.as_view(), name='home_products_list'),
    path('products/<slug:slug>', CardDetailView.as_view(), name='card_detail'),
]
