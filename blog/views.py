from django.shortcuts import render,redirect
from .models import Blog_details
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import new_form

def sign_up(request):
    if request.method=='POST':
        form=new_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created Succesfully')
            return redirect('login')
    form=new_form()
    return render(request,'blog/signup.html',{'form':form})
def index(request):
    print(request.user)
    data=Blog_details.objects.order_by('-date_pub').exclude(id=2)
    p=Paginator(data,2)
    page = request.GET.get('page')
    data = p.get_page(page)
    return render(request,'blog/blog.html',{'data':data})

def test(request):
    return render(request,'blog/test.html')

@login_required
def profile(request):
    return render(request,'blog/post.html')

def get_post(request,post_name,post_id):
    data=Blog_details.objects.get(id=post_id)
    content={
    'data':data
    }
    return render(request,'blog/get_post.html',content)
def search(request):
    if request.method == 'POST':
        name=request.POST['search']
        print(name)
        data=Blog_details.objects.filter(title=name)
        if data:
            content={
            'data':data
            }
            return render(request,'blog/search.html',content)

        else:
            messages.error(request,"post not found")
            return render(request,'blog/search.html',)
    return render(request,'blog/blog.html')
