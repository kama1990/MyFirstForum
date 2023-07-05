from django.db import models
from django.contrib.auth. models import User


class Posts(models.Model):
    title = models.CharField(max_length=200)
    dec = models.TextField(blank=True)
    createDate = models.DateTimeField(auto_now_add=True) # automatically filled by Django during creation
    # categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    image = models.ImageField(upload_to='images/',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Creating many to many relationship with User model
    topics = [
        ('', 'Wybierz temat'),
        ('sold', 'Sprzedam'),
        ('buy', 'Kupię'),
        ('rent', 'Wypożyczę'),
        ('look', 'Szukam'),
        ('else', 'Inne'),
    ] 
    topic = models.CharField(max_length=4, choices=topics, default='')
    
  
    def __str__(self):
        return f'{self.title} | {self.user}'
    
    
# we need to define the user of each commnet
class PostComment(models.Model):
    content = models.TextField() # content of the commnet
    createDate = models.DateTimeField(auto_now_add=True) # # we need to know when did user post the commnet. date will be add automatically  
    image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # we need to create realtionship between the commnet and user .
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments') # each post should has its commnet , we need to add realtionship between post model and commnet model

    def __str__(self):
        return self.desc[:12]


    # class Meta:
    #     ordering = ('createDate',)

    # def __str__(self):
    #     return 'Comment {} by {}'.format(self.content, self.user)

    
   
