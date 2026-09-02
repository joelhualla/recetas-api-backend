from django.shortcuts import render

def bienvenida(request):
    return render(request, 'bienvenida.html')

def error_404_view(request, exception=None):
    return render(request, '404.html', status=404)