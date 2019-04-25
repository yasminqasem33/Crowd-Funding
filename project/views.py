from django.shortcuts import render
from .models import Project
from .forms import *
from .models import *



# Create your views here.
def list_cates(request):
    categories = Category.objects.all()
    categories_names = list()
    for category in categories:
        categories_names.append(category.name)
        print(category.name)
    return render(request, 'project/list_cates', {"categories": categories})

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


