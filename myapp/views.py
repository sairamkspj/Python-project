from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse
from .models import Blog

def home(request):
    data=Blog.objects.all()
    return render(request,'base.html',{'data': data})
def demo(request):
    return HttpResponse("welocome to demo")
def dev(request):
    if request.method == 'POST':
       title=request.POST.get('title')
       fname=request.POST.get('fname')
       lname=request.POST.get('Iname')
       image=request.FILES.get('myfile')

       k=Blog.objects.create(title=title,fname=fname,lname=lname,image=image)

       k.save()
    return render(request,'sai.html')
