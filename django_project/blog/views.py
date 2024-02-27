from django.shortcuts import render
from .models import Post
# Create your views here.

posts=[
    {
        'author':'mohammad',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'August 27, 2018'
    },
      {
        'author':'Ahmad',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'April 10, 2020'
    }
]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})