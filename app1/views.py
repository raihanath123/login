from django.shortcuts import render
from django.http import HttpResponse
def LoginFun(request):
 return render(request,'login.html')


