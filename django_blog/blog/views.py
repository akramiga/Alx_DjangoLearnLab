from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post

#Create your views here.
class Login(LoginView):
    template_name = 'blog/login.html'

class Logout(LogoutView):
    template_name = 'blog/logout.html'

# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse('login.html')
#     template_name='blog/register.html'
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('blog/profile.html')  # Redirect to homepage after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})






# List all  posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['published_date']

# Display one post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

# Create a new  post for only uthenticated users 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog_post = self.get_object()
        return self.request.user == blog_post.author  # Ensure only the author can edit

# Delete a post 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog-list')

    def test_func(self):
        blog_post = self.get_object()
        return self.request.user == blog_post.author
