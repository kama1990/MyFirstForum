from django import forms
from .models import Posts

# the user have to create new posts 
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Posts # we used here Posts model from models
        fields = ('title', 'dec', 'published', 'image' ) # we add here filds which can be complete by user
        # we have also another 2 diffrent options:
        # exclude = ('createDate','published','user') # Show all fields from model except these
        # fields = '__all__' # Show all fields from model
        
