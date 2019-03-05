from django.shortcuts import render

def view_403(request):
    return render(request,'errors/403.html',status=403)

def view_400(request):
    return render(request,'errors/400.html',status=400)