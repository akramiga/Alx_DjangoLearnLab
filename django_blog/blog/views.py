from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
class LoginView(LoginView):
    template_name = 'blog/login.html'

class LogoutView(LogoutView):
    template_name = 'blog/logout.html'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('/blog/base.html')  # Redirect to homepage after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})