from django.db import models
from django.contrib.auth. models import User


# Create your models here.


# we need to define the user of each commnet
# class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # we need to create realtionship between the commnet and user . 
    # date = models.DateField(auto_now_add=True) # we need to know when did user post the commnet. date will be add automatically
    # post = models.ForeignKey('Posts', on_delete=models.CASCADE) # each post should has its commnet , we need to add realtionship between post model and commnet model
    # content = models.TextField() # content of the commnet

    # def __str__(self):
    #     return self.user.username

    


class Posts(models.Model):
    title = models.CharField(max_length=200)
    dec = models.TextField(blank=True)
    createDate = models.DateTimeField(auto_now_add=True) # automatically filled by Django during creation
    # categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    image = models.ImageField(upload_to='images/',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Creating many to many relationship with User model

  

    def __str__(self):
        return f'{self.title} | {self.user}'
    
# we need to define the user of each commnet

    # user = models.ForeignKey(User, on_delete=models.CASCADE) # we need to create realtionship between the commnet and user . 
    # date = models.DateField(auto_now_add=True) # we need to know when did user post the commnet. date will be add automatically
    # post = models.ForeignKey('Posts', on_delete=models.CASCADE) # each post should has its commnet , we need to add realtionship between post model and commnet model
    # content = models.TextField() # content of the commnet
class Comment(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    user = models.CharField(max_length=80)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering = ('createDate',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user)

    
   
