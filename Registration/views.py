from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Posts, PostComment
from .forms import PostForm, CommentForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


def post(request):
    posts = Posts.objects.all().order_by('-createDate')
    return render(request, 'post.html', {'posts':posts})


def myOwn(request):
    posts = Posts.objects.filter(user=request.user)
    return render(request, 'myOwn.html', {"posts":posts})


def createNewPosts(request):
    if request.method == 'GET': # When used GET method eg. web loading, create empty creation form
        return render(request, 'createNewPosts.html', {'form': PostForm()})

    else:
        form = PostForm(request.POST, request.FILES) # create POstForm and fill it with request data, requests.FILEDS are neccesery for image which user would like to upload
        if form.is_valid(): # if data is valid
            post = form.save(commit=False) # it create post but it will be not save yet
            post.user = request.user # we have to add user
            post.save() # now we can save it
            return redirect('post') # Redirecting user to localhost:8000/posts
        # we have to remeber about - what if somethong goes wrong
        else:
            error = 'Something went wrong'
            # the second chance for user
            return render(request, 'createNewPosts.html', {'form': PostForm(), 'error': error})
        

# we want to edit the posts        
def detail(request, postId):
    # Use get() to return an object, or raise a Http404 exception if the object does not exist.
    post = get_object_or_404(Posts, pk=postId, user=request.user)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'detail.html', {'post':post, 'form':form})
    else:
        # we want to fillin postformfor exist post , user is there  /  user jest zaciagny z instancji/
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            #zawsze return na koniec widoku
            return redirect('post')
        # we want to gives one more chance to user
        else:
            error = "Something went wrong. Please try one more time"
            return render(request, 'detail.html', {'post':post, 'form':form, 'error':error})
        

def deletePost(request, postId):
    post = get_object_or_404(Posts, pk=postId, user=request.user)
    post.delete()
    return redirect('post')
    # return render(request, 'deletePost.html') # we could use retur redirect('posts' ), we have to know where we want to put user through after delete post . posts is name from urls. but we wanted , that user knew that he is delete post .

# we want to open each post , after below view , we create html file and path in urls
def detailPost(request, postId):
    post = get_object_or_404(Posts, pk=postId)
    comments = post.comments.all().order_by('-createDate') # comments -= related_name
    return render(request,'detailPost.html', {'post':post, 'comments':comments})


def createAnswerPost(request, postId):
    post = get_object_or_404(Posts, pk=postId)
    if request.method == 'GET':
        return render(request, 'createAnswerPost.html', {'form':CommentForm(), 'post':post})
    else:
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = request.user
            comments.post = post
            comments.save()
            return redirect('http://127.0.0.1:8000/'+str(postId)+'/detailPost/')
        
        else:
            error = "Something went wrong. Please try again!"
            return render(request, 'createAnswerPost.html', {'form':CommentForm(), 'post':post, 'error':error})
        

def editAnswerPost(request, commentId):
    comment = get_object_or_404(PostComment, pk=commentId, user=request.user)
    post = get_object_or_404(Posts, pk=comment.post.id)
    if request.method == 'GET':
        form = CommentForm(instance=comment)
        return render(request, 'editAnswerPost.html', {'form':form, 'post':post, 'comment':comment})
    else:
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/'+str(post.id)+'/detailPost/')
        else:
            error = "Something went wrong. Please try again!"
            return render(request, 'editAnswerPost.html', {'form':form, 'post':post, 'comment':comment, 'error':error})
        
    







