from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recetas.urls')),
]

# Controlador para la página de error 404 personalizada
handler404 = 'recetas.views.error_404_view'
