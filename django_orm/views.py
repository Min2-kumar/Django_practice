from django.shortcuts import render
from .models import Student

# Create your views here.

def index(request):
    return render(request,'django_orm/index.html')


def submit(request):
    data = request.POST
    if request.method == "POST":
        name = data['name']
        age = data['age']
        email = data['email']
        marks = data['marks']
        Student.objects.create(stuName=name, stuAge=age, stuEmail = email, stuMarks = marks)
    return render(request,'django_orm/index.html')