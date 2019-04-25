from django.shortcuts import render
from .models import Project

# Create your views here.
def showOne(request,id):
    project = Project.objects.get(id=id)
    print(project)
    return render(request, 'project/showOne.html', {"project": project})


