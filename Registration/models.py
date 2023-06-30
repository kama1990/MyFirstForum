from django.db import models
from django.contrib.auth. models import User
# Create your models here.

# class Category(models.Model):
#     title = models.CharField(max_length=20)

#     def __str__(self):
#         return self.title
    
    # class Meta:
    #     verbose_name = "Category"
    #     verbose_name_plural = "Categories"


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
