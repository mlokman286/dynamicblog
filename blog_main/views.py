from django.shortcuts import render
from blogs.models import Blogs, Category

def home(request):
    categories = Category.objects.all()
    fetured_post = Blogs.objects.filter(is_fetured = True)
    context = {
        'categroies':categories,
        'fetured_post':fetured_post,
        }
    return render(request,'home.html',context)