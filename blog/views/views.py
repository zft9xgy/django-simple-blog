from django.shortcuts import render,redirect, get_object_or_404
from blog.models import Post, Tag, Profile
from blog.forms import PostForm, TagForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    posts = Post.objects.filter(status='published')[:3]
    context = {
        'posts': posts,
    }
    return render(request,'uniques/index.html',context)

def demo(request):
    return render(request,'uniques/demo.html')

def blog(request):
    posts = Post.objects.filter(status='published')

    context = {
        'posts': posts,
    }
    return render(request,'blog/blog.html',context)


def single(request,slug):

    post = Post.objects.get(slug=slug)

    context = {
        'post':post,
    }

    return render(request,'blog/single.html',context)

@login_required(login_url='user-login')
def adminPanel(request):

    posts = Post.objects.all()
    tags = Tag.objects.all()
    profiles = Profile.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
        'profiles': profiles,
    }
    return render(request,'blog/admin-panel.html',context)

@login_required(login_url='user-login')
def createSingle(request):

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-panel')

    context = {
        'form': form,
    }
    return render(request,'blog/create-single.html',context)

@login_required(login_url='user-login')
def editSingle(request,slug):

    post = Post.objects.get(slug=slug)

    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request,'blog/create-single.html',context)

@login_required(login_url='user-login')
def deleteSingle(request,slug):

    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect("/")
    
    context = {
        'object': post,
    }
    return render(request,'blog/delete-object.html',context)
    


## TAG CRUD

def tagView(request,slug):

    tag = get_object_or_404(Tag, slug=slug)
    # Filtrar publicaciones que contienen esta etiqueta
    posts = Post.objects.filter(tags__slug__icontains=slug)

    context = {
        'posts': posts,
        'tag': tag,
    }
    return render(request,'blog/tag.html',context)

@login_required(login_url='user-login')
def createTag(request):

    form = TagForm()

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta creada correctamente')
            return redirect('admin-panel')

    context = {
        'form': form,
    }

    return render(request,'blog/create-single.html',context)

@login_required(login_url='user-login')
def editTag(request,slug):
    
    tag = Tag.objects.get(slug=slug)

    form = TagForm(instance=tag)

    if request.method == 'POST':
        form = TagForm(request.POST,instance=tag)
        if form.is_valid():
            form.save()
            return redirect('admin-panel')

    context = {
        'form': form,
    }
    return render(request,'blog/create-single.html',context)

@login_required(login_url='user-login')
def deleteTag(request,slug):

    tag = Tag.objects.get(slug=slug)

    if request.method == 'POST':
        tag.delete()
        return redirect("/")
    
    context = {
        'object': tag,
    }
    return render(request,'blog/delete-object.html',context)


# # user login and logout 
# def userLogin(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             # A backend authenticated the credentials
#             login(request,user)
#             messages.success(request,'Usuario logeado correctamente.')
#             next = request.GET.get('next')
#             return redirect(next or 'home')
#         else:
#             # No backend authenticated the credentials
#             messages.error(request,'username or password wrong.')
#             print('username or password wrong')


#     return render(request,'users/login.html')


# @login_required(login_url='user-login')
# def userLogout(request):

#     logout(request)
#     messages.info(request, 'User was logged out!')
#     return redirect('home')
