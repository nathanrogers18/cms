from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
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


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('login success!')
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('forum:index'))
        else:
            print("invalid login")
        # Return an 'invalid login' error message.

    return render(request, 'forum/login_view.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('forum:index')
