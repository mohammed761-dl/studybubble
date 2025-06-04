from .forms import SignUpForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")
