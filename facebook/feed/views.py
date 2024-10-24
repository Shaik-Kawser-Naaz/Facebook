from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def func1(request):
    result=User.objects.all()
    return render(request,'index.html',{'res':result})
def func2(request):
    return render(request,'about.html')
def func3(request):
    return render(request,'contact.html')
def func4(request):
    return render(request,'posts.html')
def func5(request):
    return render(request,'login.html')
def func6(request):
    if request.method=="POST":
        usern=request.POST.get('sname')
        check=User.objects.filter(username=usern).exists()
        print(check)
        k=User.objects.filter(username=usern)
        print(k)
    return render(request,'forms.html',{'res':check,'list':k})

