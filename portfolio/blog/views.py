from django.shortcuts import render

# Create your views here.
from blog.models import Post

def blog_index(request):
    """View for the home page - renders 'blog_index.html' which diplays
    the blog posts in the database filtered by date """
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)


def blog_category(request, category):
    """View for each of the posts associated with the category passed in - renders 'blog_category.html' """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)
    

def blog_detail(request, pk):
    """View for each of the posts accessed by their primary keys - renders 'blog_detail.html' """
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }

    return render(request, "blog/blog_detail.html", context)
