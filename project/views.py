from django.shortcuts import render
from .models import Project
from .forms import *
from .models import *
import collections
import operator


# Create your views here.
def avg_rate(id):
    mkm = 1
    total_rate = 0
    rates = Rate.objects.all().filter(project=id)
    for rate in rates:
        total_rate = (total_rate + rate.rate)
    if len(rates) == 0:
        total_rate = total_rate / mkm
    else:
        total_rate = total_rate / len(rates)
    return total_rate


def home(request):
    projects_avg_rate = {}
    projects_avg_rate2 = {}
    highly_rated = []
    key = []
    value = []
    projects = Project.objects.all()
    for project in projects:
        key.append(project.id)
        value.append(avg_rate(project.id))
    projects_avg_rate = dict(zip(key, value))
    print(projects_avg_rate)
    print("data")
    # to sort the dict by value
    sorted_d = sorted(projects_avg_rate.items(), key=operator.itemgetter(0))
    # to convert the list of tuple into dict
    for a, b in sorted_d:
        projects_avg_rate2.setdefault(a, b)
    print(projects_avg_rate2)
    print(sorted_d)
    for i in projects_avg_rate.keys():
        highly_rated.append(Picture.objects.all().filter(project=i)[0])
    for i in highly_rated:
        print(i.picture)
    print(highly_rated)
    print("highly_rated")



    latest_projects = Project.objects.all().order_by('-start_date')
    featured_projects = Project.objects.all().filter(featured=True).order_by('-start_date')
    print(featured_projects[0].title)
    rate = Rate.objects.all().filter(project=1)
    print("rate")
    print(rate[0])
    return render(request, 'project/home.html', {"featured_projects": featured_projects, "latest_projects":latest_projects, "highly_rated":highly_rated})

def category(request,id):
    category = Category.object.get(id=id)
    projects = Project.objects.all().filter(category=category)
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
    if request.method == 'POST':

        comment = Form_comment(request.POST)
        donation = Form_donation(request.POST)
        if comment.is_valid():
            print("valid")
        comment_obj = Comment()
        comment_obj.user_id = 1
        comment_obj.project_id = id
        comment_obj.text = request.POST['text']
        comment_obj.save()
        if donation.is_valid():
            donation_obj = Donation()
            donation_obj.user_id = 1
            donation_obj.project_id = id
            donation_obj.donation = request.POST['donation']
            donation_obj.save()

    else:


        comment = Form_comment()
        donation = Form_donation()

    return render(request, 'project/showOne.html', {"project": project,"form1": comment ,"form2":donation})


