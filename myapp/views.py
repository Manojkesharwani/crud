from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import MYBLOGAPP
from .forms import mydata

# Create your views here.

def index(request):
    res=MYBLOGAPP.objects.all()
    return render(request,'myapp/index.html',{"data":res})



def blog(request,id):
    post_request=get_object_or_404(MYBLOGAPP,id=id)
    return render(request,'myapp/blog.html',{"post":post_request})



def edit_data(request,id):
    post_data=get_object_or_404(MYBLOGAPP,id=id)
    if request.method=='POST':
        form_data=mydata(request.POST,instance=post_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    else:
        form_data=mydata(instance=post_data)
        myinfo={"form_data":form_data}
    return render(request,'myapp/edit.html',myinfo)


def post_delete(request,id):
    data=get_object_or_404(MYBLOGAPP,id=id)
    data.delete()
    return redirect('home')


def about(request):
    if request.method=='POST':
        data=mydata(request.POST)
        if data.is_valid():
            res=data.save()
            res.save()
            return redirect('home')
    else:
        res=mydata()
        result={"res":res}
    return render(request,'myapp/about.html',result)





