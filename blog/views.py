from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    """Test function-based view"""
    posts = Post.objects.all()
    print(f'{posts}')
    post_list = [{'title': post.title, 'content': post.content,
                'date_posted': post.date_posted, 'author': post.author} for post in posts]

    context = {'post_list': post_list}
    return render(request, 'base.html', context)
