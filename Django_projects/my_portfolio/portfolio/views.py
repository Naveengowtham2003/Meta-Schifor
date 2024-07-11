from django.shortcuts import render, redirect
# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm


def home(request):
    return render(request, 'base.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogPostForm()
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'form': form, 'posts': posts})
