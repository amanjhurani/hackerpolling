from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def index(request):
    users = request.user
    context = {
            'users': users,
        }
    return render(request, 'index.html',context)


@login_required
def hacker_list(request):
    if request.method == 'POST':
        return HttpResponse("<h1>VOTED</h1>")
    else:
        users = User.objects.all()
        context = {
                'users': users,
            }
        return render(request, 'hackerlist.html',context)

def user_detail(request):
      hacker = User.objects.get(id=int(request.GET['user']))
      context ={
          'hacker' : hacker
      }
      return render(request,'userdetail.html', context)

def vote(request):
    if request.user.vote_given == False:
        userv = User.objects.get(id=int(request.GET['user']))
        userv.votes = userv.votes + 1
        userv.save(update_fields=['votes'])
        context = {
            'user' : userv
        }
        user = User.objects.get(email=request.user.email)
        user.vote_given = True
        user.vote_given_to = userv.username
        user.save(update_fields=['vote_given','vote_given_to'])
        return render(request,'votes.html',context)
    else:
        user = request.user.username
        return HttpResponse("<center><h1>You have already given a vote. Go Back</h1></center>")
