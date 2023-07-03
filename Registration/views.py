from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Comment
from .forms import PostForm, CommentForm


# Create your views here.

# Home page
def home(request):
    allPosts = Posts.objects.all().order_by('-createDate')
    return render(request, 'home.html', {"allPosts":allPosts})


def posts(request):
    usersPosts = Posts.objects.all().order_by('-createDate')
    return render(request, 'posts.html', {'posts':usersPosts})

def createNewPosts(request):
    if request.method == 'GET': # When used GET method eg. web loading, create empty creation form
        return render(request, 'createNewPosts.html', {'form': PostForm()})

    else:
        form = PostForm(request.POST, request.FILES) # create POstForm and fill it with request data
        if form.is_valid(): # if data is valid
            post = form.save(commit=False) # it create post but it will be not save yet
            post.user = request.user # we have to add user
            post.save() # now we can save it
            return redirect('posts') # Redirecting user to localhost:8000/posts
        # we have to remeber about - what if somethong goes wrong
        else:
            error = 'Something went wrong'
            # the second chance for user
            return render(request, 'createNewPosts.html', {'form': PostForm(), 'error': error})
        
def my(requst):
    pass

# we want to edit the posts        
def detail(request, postId):
    post = get_object_or_404(Posts, id=postId, user=request.user)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'detail.html', {'post':post, 'form':form})
    else:
        # we want to fillin postformfor exist post , user is there  /  user jest zaciagny z instancji/
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            #zawsze return na koniec widoku
            return redirect('posts')
        # we want to gives one more chance to user
        else:
            error = "Something went wrong. Please try one more time"
            return render(request, 'detail.html', {'post':post, 'form':form, 'error':error})
        

def deletePost(request, postId):
    post = get_object_or_404(Posts, id=postId, user=request.user)
    post.delete()
    return render(request, 'deletePost.html') # we could use retur redirect('posts' ), we have to know where we want to put user through after delete post . posts is name from urls. but we wanted , that user knew that he is delete post .


def myComments(request, postId):
    pass
    

