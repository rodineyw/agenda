
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/agenda/')),
    path('agenda/', views.lista_eventos),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('admin/', admin.site.urls),
]
