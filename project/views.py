from django.shortcuts import *
from .forms import *
from .models import *



# Create your views here.
def category(request,id):
    category = Category.objects.get(id=id)
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
    # comments = Comment.objects.get()
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


    else:


        comment = Form_comment()
        donation = Form_donation()

    return render(request, 'project/showOne.html', {"project": project,"form1": comment,"form2": donation})


def addDonate(request,id):
    if request.method == 'POST':
        donation = Form_donation(request.POST)

        print('inside donation')
        print(id)
        if donation.is_valid():
            donation_obj = Donation()
            donation_obj.user_id = 1
            donation_obj.project_id = id
            donation_obj.donation = request.POST['donation']
            donation_obj.save()

        return redirect('show_project', id=id)