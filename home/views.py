from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def error404(request):
    return render(request, 'home/404.html', status=404)