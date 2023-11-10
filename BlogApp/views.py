from django.shortcuts import render,redirect
from .forms import loginForm,registerForm,createBlogForm,updateBlogForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone

# Create your views here.



def welcome(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))

    return render(request,'welcome.html',{'view':'welcome'})


def loginView(request):

    message = ""

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))

    if request.method == 'POST':
        login_form = loginForm(data=request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user) # saves the user’s ID in the session, using Django’s session framework.
            return HttpResponseRedirect(reverse('main'))

        else:
              message = "Username or password is incorrect"

    login_form = loginForm()
    return render(request,'login.html',{'userForm':login_form,'message':message})


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))
    if request.method == 'POST':
        register_form = registerForm(data=request.POST)

        if register_form.is_valid():

            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(user.password)
                user.save()
                return HttpResponseRedirect(reverse('login'))


    else:
        register_form = registerForm()

    return render(request,'register.html',{'registerForm':register_form})

@login_required
def main(request):
    blogs = Blog.objects.all()
    has_blog = Blog.objects.filter(user=request.user)
    if has_blog.count() > 0: # If user has blog
        user_blog = Blog.objects.get(user=request.user)
        return render(request, 'main.html',{'blogs':blogs,'id':user_blog.pk})
    else: # If blog not exist
        return render(request, 'main.html', {'blogs': blogs})



@login_required
def create(request):
    user = request.user # To get username and email
    date = timezone.now() # For date field
    submit_text = 'Create' # Text for submit button, create or update

    if request.method == 'POST':
        form = createBlogForm(request.user, request.POST, request.FILES) # request.user to check if user has blog

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('blog',pk=form.pk)
    else:
        form = createBlogForm(user=request.user)

    return render(request,'createUpdate.html',{'form':form,'user':user,'date':date,'submit_text':submit_text})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    has_blog = Blog.objects.filter(user=request.user) # If user has blog
    if has_blog.count() > 0:
        user_blog = Blog.objects.get(user=request.user)
        return render(request, 'blog.html', {'Blog': blog, 'id': user_blog.id, 'user': request.user})
    else:
        return render(request,'blog.html',{'Blog':blog})

@login_required
def update(request,pk):
    user_blog = Blog.objects.get(user=request.user) # Get the user's blog
    user = request.user # To get username and email
    date = timezone.now() # For date field
    submit_text = 'Update' # Text for submit button, create or update

    if request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        form = updateBlogForm(request.POST,request.FILES,instance=blog) # Create form instance and populate with request.POST data and if instance is supplied, save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model:
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = updateBlogForm(request.GET)
    return render(request,'createUpdate.html',{'user':user,'form':form,'id':user_blog.id,'date':date,'submit_text':submit_text})


@login_required
def delete(request,pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('main')