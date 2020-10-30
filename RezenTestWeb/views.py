#视图函数,返回index.html页面
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


#####from django.shortcuts import render

# Create your views here.

####def RezenTestWeb(request):
####return render(request,'RezenTestWeb.html')


