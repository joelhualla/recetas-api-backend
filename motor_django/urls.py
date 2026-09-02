from django.contrib import admin
from django.urls import path
from recetas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
]