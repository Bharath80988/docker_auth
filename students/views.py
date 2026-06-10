from django.shortcuts import render, redirect
from .models import Student

def home(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email = request.POST['email'],
        )
        return redirect('/')
    
    students = Student.objects.all()

    return render(
        request,'home.html',{'students':students}
    )