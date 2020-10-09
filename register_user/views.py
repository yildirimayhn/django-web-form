from django.shortcuts import render
from register_user.models import Userreg
from django.contrib import messages


def Userregistration(request):
    if request.method == 'GET':
        return render(request, 'Index.html')
    elif request.method=='POST':
        if request.POST.get('uname') and request.POST.get('usurname') and request.POST.get('uemail') and request.POST.get('uphone'):
            saverecord=Userreg()
            saverecord.uname=request.POST.get('uname')
            saverecord.usurname=request.POST.get('usurname')
            saverecord.uemail=request.POST.get('uemail')
            saverecord.uphone=request.POST.get('uphone')
            saverecord.save()
            messages.success(request,"New User Registrated Successfully")
            return render(request,'Index.html')
        
