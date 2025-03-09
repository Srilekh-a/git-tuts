from django.shortcuts import render,HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from.forms import StudentInfoForm
from django.db.models import Q

def list_student(request):
    student =Student.objects.all()
    return render(request,'list_student.html',{"student":student})
def update_student(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        fm=StudentInfoForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        student=Student.objects.get(pk=id)
        fm=StudentInfoForm(instance=student)
    # student =Student.objects.get(pk=id)
    # fm =StudentInfoForm(instance=student)
    return render(request,'update_student.html',{"form":fm})

def delete_student(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")
    
def add_student(request):
    if request.method=="POST":
        fm=StudentInfoForm(request.POST)
        fm.save()
        return HttpResponseRedirect("/")
    else:

        fm =StudentInfoForm()
    return render(request, "add.html", {"form":fm} )
def search_student(request):
    if request.method=="POST":
        search= request.POST.get("output")
        student=Student.objects.all()
        std=None
        if search:
            std=student.filter(
                Q(fname__icontains=search)|
                Q(lname__icontains=search)|
                Q(email__icontains=search)|
                Q(branch__icontains=search))
        return render(request,"list_student.html",{'student':std})
    else:
        return HttpResponse("An error occured")
               
                
   
