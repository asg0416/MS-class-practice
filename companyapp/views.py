from django.shortcuts import render
from .models import UserInfo
from .forms import CamForm

# Create your views here.
def index(request):
    context = dict()
    request.POST.get('mydata')
    all_UserInfo = UserInfo.objects.all() 
    context['all_UserInfo'] = all_UserInfo
    return render(request, 'index.html',context)

def second(request):
    return render(request, 'second.html')

def create(request):
    context=dict()
    context['camform'] = CamForm()
    if request.method =="POST":
        myform = CamForm(request.POST.request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('index')
        else:
            context['camform']= myform
    return render(request,'second.html',context)