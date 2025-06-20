from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')


from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace with your home URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
