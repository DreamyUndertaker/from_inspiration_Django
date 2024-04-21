from django.conf.urls.static import static
from django.urls import path

from from_inspiration import settings
from home.views import CardDetailView, ProductListView

urlpatterns = [
    path('<slug:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('', ProductListView.as_view(), name='home'),
    path('products/<slug:slug>', CardDetailView.as_view(), name='card_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
