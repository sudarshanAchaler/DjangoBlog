from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    postCategory = models.CharField(max_length=25, null=False, blank=False)
    title = models.CharField( max_length=100, null=False, blank=False)
    dateAdded = models.DateField( auto_now_add=True)
    content = models.TextField()
    shortDescription = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField( blank=True, default="")
    likes = models.ManyToManyField(User, default="", blank=True)

    def __str__(self):
        temp= str(self.title) + ' on '+ str(self.dateAdded)
        return temp

    @property
    def imageURL(self):
        try:
            url=self.thumbnail.url
        except:
            url='/images/testThumb.jpg'
        return url

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return '{}-{}-{} '.format(self.user,self.post,self.body)


class PostDraft(models.Model):
    email = models.CharField(max_length=80)
    username = models.CharField(max_length=50)
    draftLink= models.CharField(max_length=100)
    note = models.TextField( null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.email, self.username)