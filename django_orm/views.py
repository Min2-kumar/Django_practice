from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

# def index(request):
#     return render(request,'django_orm/index.html')


def index(request):
    id = request.GET.get('id')
    if id:
        student = Student.objects.get(id=id)
    return render(request,'django_orm/index.html', {'students': Student.objects.all(), 'student': student if id else None})


# def submit(request):
#     data = request.POST
#     if request.method == "POST":
#         name = data['name']
#         age = data['age']
#         email = data['email']
#         marks = data['marks']
#         Student.objects.create(stuName=name, stuAge=age, stuEmail = email, stuMarks = marks)
#     return render(request,'django_orm/index.html')


def submit(request):
    data = request.POST
    id = data.get('id')
    if id:
        s = Student.objects.get(id=id)
    else:
        s = Student()
    s.stuName=data.get('name')
    s.stuAge=data.get('age')
    s.stuEmail = data.get('email')
    s.stuMarks = data.get('marks')
    s.save()
    return render(request,'django_orm/thanks.html', {'students': Student.objects.all()})


def delete(request, stu_id):
    Student.objects.filter(id=stu_id).delete()
    return redirect('/')
