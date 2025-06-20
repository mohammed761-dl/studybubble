from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
import traceback

def signup(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    except Exception as e:
        traceback.print_exc()
        raise e


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")
