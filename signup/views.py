from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .models import SignUpForm

def sign(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        context_instance=RequestContext(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/camp/2016/signup/thanks/')
        else:
            return render(request, 'signup/signup.html', {'form': form})
        
    else:
        form = SignUpForm()
        context_instance=RequestContext(request)
    return render(request, 'signup/signup.html', {'form': form})

def thanks(request):
    return render(request, 'signup/thanks.html')