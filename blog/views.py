from django.shortcuts import render

posts = [
    {
        'author': 'Jaskirat',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 10, 2021'
    },
    {
        'author': 'Random',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 11, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})