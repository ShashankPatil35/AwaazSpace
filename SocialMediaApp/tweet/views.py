from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

#to list tweets
def tweet_list(request):
    #Tweet.objects.all(): This queries the Tweet model to retrieve all tweet objects from the database.
    tweets = Tweet.objects.all().order_by('-created_at')#order_by('-created_at'): This orders the retrieved tweet objects by the created_at field in descending order (the - before created_at indicates descending order). This means the most recently created tweets will be listed first.
    return render(request,'tweet_list.html',{'tweets':tweets}) #tweets pases queryset to template(i.e tweet_list.html)

@login_required
def tweet_create(request):
    if request.method=="POST": #request method is POST (indicating that form data has been submitted), 
        form = TweetForm(request.POST,request.FILES)    
        if form.is_valid():
            tweet = form.save(commit=False) #Temporarily saves the form data without committing to the database (commit=False).
            tweet.user = request.user #Assigns the current logged-in user (request.user) to the tweet.
            tweet.save() #Saves the tweet to the database.
            return redirect('tweet_list') 
            # return redirect('tweet_form') 
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})    

@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user) #Retrieves the tweet object with the given tweet_id from the database.
                                                #If the tweet does not exist, it raises a 404 error.
    if request.method=="POST":
        form = TweetForm(request.POST, request.FILES,instance=tweet)#Initializes the form with the submitted data and files, binding it to the tweet instance.
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})    

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
