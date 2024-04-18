from django.template.context_processors import static
from django.urls import path

from from_inspiration import settings
from home.views import ProductsList, CardDetailView

urlpatterns = [
    path('', ProductsList.as_view(template_name='home/list_of_pictures.html'), name='home'),
    path('products/<slug:slug>', CardDetailView.as_view(), name='card_detail'),
]
