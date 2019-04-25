from django.contrib import admin
from .models import Project
from .models import Category
from .models import Comment
from .models import Picture
from .models import  Report_comment
from .models import Report_project
from .models import Donation
from .models import Tag
from .models import Rate


admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Picture)
admin.site.register(Report_comment)
admin.site.register(Report_project)
admin.site.register(Donation)
admin.site.register(Tag)
admin.site.register(Rate)
# Register your models here.
