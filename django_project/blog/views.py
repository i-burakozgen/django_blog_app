from django.shortcuts import render
from django.http import HttpResponse
from .models import Post    
#DUMMY DATA 
# """ posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ] """

# home funtion gonna handle the traffic from homepage to blog (user gonna see what we want the see user sent the this route)
def home(request):
    #TO PASS THE DATA WE CREATE A DIC
    context = {
        'posts':Post.objects.all()
    }
    # this for plain http return HttpResponse('<h1>Blog home page <h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog about page <h1>')
    return render(request, 'blog/about.html', {'title': 'About'})



# Create your views here.
