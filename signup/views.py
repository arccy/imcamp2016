from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .models import SignUpForm

def sign(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signup/thanks/')
        else:
            return render(request, 'signup/signup.html', {'form': form})
        
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})

def thanks(request):
    return render(request, 'signup/thanks.html')