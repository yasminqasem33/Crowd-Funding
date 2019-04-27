from django.db import models
from user.models import User
from django.template.defaultfilters import slugify

def get_image_filename(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)
class Category(models.Model):
    name = models.CharField(max_length=100 )

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    total_target = models.BigIntegerField()
    # featured = models.BooleanField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Picture(models.Model):
#     project = models.ForeignKey(Project,on_delete=models.CASCADE)
#     picture = models.ImageField(upload_to='project/images/%Y/%m/%d/')

class Images(models.Model):
    project = models.ForeignKey(Project, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')


class Report_comment (models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)



class Report_project(models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class Donation(models.Model):
    donation =models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class Rate(models.Model):
    rate= models.IntegerField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

