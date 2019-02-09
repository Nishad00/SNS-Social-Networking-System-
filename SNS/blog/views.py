from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'Nishad',
        'title' : 'blog post 1',
        'content':'first post',
        'date_posted' :'March 19, 2019'
    },
    {
        'author' : 'rashmi',
        'title' : 'blog post 2',
        'content':'second post',
        'date_posted' :'March 19, 2019'
    }
]

def home(request):

    context = {
        'posts':posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
