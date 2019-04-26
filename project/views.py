from django.shortcuts import *
from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.
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
    try:
        comments = Comment.objects.filter(project_id=id)
    except Comment.DoesNotExist:
        comments = None
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
        report_pro = Form_reportProject()
        report_com = Form_reportComment()



    return render(request, 'project/showOne.html', {
        "project": project,
        "form1": comment,
        "form2": donation,
        "form3":report_pro,
        "form4": report_com,
        "comments": comments})


def addDonate(request,id):
    if request.method == 'POST':
        donation = Form_donation(request.POST)
        totaltarget = Project.objects.values_list('total_target').get(id=id)[0]
        print(totaltarget)
        print('inside donation')
        if donation.is_valid():
            if int(request.POST['donation']) + calcDontion(id) < totaltarget:

                donation_obj = Donation()
                donation_obj.user_id = 1
                donation_obj.project_id = id
                donation_obj.donation = request.POST['donation']
                donation_obj.save()
            else:
                messages.error(request, 'Project reach the total target')
            return redirect('show_project', id=id)


def report_pro(request,id):
    if request.method == 'POST':
        report_pro = Form_reportProject(request.POST)
        if report_pro.is_valid():
            report_pro_obj = Report_project()
            report_pro_obj.user_id = 1
            report_pro_obj.project_id = id
            report_pro_obj.text = request.POST['text']
            report_pro_obj.save()

        return redirect('show_project', id=id)

def report_com(request,id):
    print("inside report comment")
    if request.method == 'POST':
        report_com = Form_reportComment(request.POST)
        if report_com.is_valid():
            report_com_obj = Report_comment()
            report_com_obj.user_id = 1
            report_com_obj.project_id = id
            report_com_obj.text = request.POST['text']
            report_com_obj.comment_id = request.POST['comId']
            report_com_obj.save()

        return redirect('show_project', id=id)

def calcDontion(id):
    sum=0
    donations=Donation.objects.values_list('donation').filter(project_id=id)
    try:
       for i in donations:
           sum=sum+int(i[0])
       return sum
    except Comment.DoesNotExist:
       return 0
