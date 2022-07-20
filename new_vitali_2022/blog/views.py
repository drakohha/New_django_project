from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

# class BlogListView(ListView):
#     model = Post
#     template_name = 'blog_index.html'


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'blog_detail.html'


def blog_index(request):
    posts = Post.objects.all().order_by("created_on")
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)

# def blog_detail(request,pk):
#     post= Post.objects.get(pk=pk)
#     context = {
#         'posts': post
#     }
#     return render(request, 'blog_detail.html', context)
