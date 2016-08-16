from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    posts = Post.objects.filter(is_published=True).order_by('time_created')
    context = {'posts': posts}
    return render(request, 'forum/index.html', context)


def user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = user.post_set.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'forum/user.html', context)
