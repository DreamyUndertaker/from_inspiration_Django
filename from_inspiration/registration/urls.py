from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path

from from_inspiration import settings
from registration.forms import UserLoginForm
from registration.views import RegisterView, CustomLoginView

urlpatterns = [
    path("signup/", RegisterView.as_view(template_name='registration/registration.html'),
         name="signup"),
    path('login/', CustomLoginView.as_view(form_class=UserLoginForm, template_name="registration/login.html"),
         name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
