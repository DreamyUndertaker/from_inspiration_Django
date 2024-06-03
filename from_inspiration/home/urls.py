from django.conf.urls.static import static
from django.urls import path
from from_inspiration import settings
from . import views
from .views import CardDetailView, ProductListView, UserProfileDetailView, UserSettingsUpdateView, search, like_card, \
    save_card

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('<slug:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('products/<slug:slug>/', CardDetailView.as_view(), name='card_detail'),
    path('user/<int:pk>/', UserProfileDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/settings/', UserSettingsUpdateView.as_view(), name='user-settings'),
    path('like/<int:card_id>/', like_card, name='like_card'),
    path('save/<int:card_id>/', save_card, name='save_card'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

