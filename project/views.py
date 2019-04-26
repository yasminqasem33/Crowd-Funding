from django.shortcuts import render
from .models import *

# Create your views here.
def category(request,id):
    category = Category.object.get(id=id)
    projects = Project.objects.get(category=category)
    return render(request, 'project/category.html', {"category": category, "projects":projects})

def list_cates(request):
    categories = Category.objects.all()
    categories_names = list()
    for category in categories:
        categories_names.append(category.name)
        print(category.name)
    return render(request, 'project/list_cates.html', {"categories": categories})

def showOne(request,id):
    project = Project.objects.get(id=id)
    print(project)
    return render(request, 'project/showOne.html', {"project": project})


