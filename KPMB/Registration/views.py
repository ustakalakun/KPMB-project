from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from Registration.models import Course, Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')

def new_course(request):
    if request.method == 'POST':
        course_code = request.POST['code']
        course_desc = request.POST['desc']
        data=Course(code=course_code,description=course_desc)
        data.save()
        dict = {
            'message':'DATA IS SAVE BRO !!!!!'
        }
    else:
        dict = {
            'message':''
        }
        
    return render(request,'new_course.html',dict)

def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse': allcourse
    }
    return render (request,'course.html',dict)

def search_course(request):
    return render(request,'search_course.html')

def search_course(request):
    if request.method == 'GET' :
        data = Course.objects.filter(code = request.GET.get('c_code'))
        dict = {
                'data': data
            }
        return render (request , "search_course.html", dict)
    else:
        return render (request , "search_course.html")
    
def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render (request , "update_course.html",dict)

def save_update_course(request,code):
    c_desc= request.POST['desc']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def new_student(request):
    if request.method == 'POST':
        id_code = request.POST['code']
        name_desc = request.POST['desc']
        address_desc = request.POST['desc']
        phone_desc = request.POST['desc']
        data=Student(ID=id_code,Name=name_desc,Address=address_desc,Phone=phone_desc)
        data.save()
        dict = {
            'message':'DATA IS SAVE '
        }
    else:
        data=Course.objects.all()
    dict = { 'c_code':data
    }
    return render(request,'new_student.html',dict)

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))

def search_by_student(request):
    if request.method == 'POST' :
        s_id = request.POST['s_id']
        data_student = Student.objects.get(id = s_id)
        data_course = Course.objects.get(code=data_student.course_code_id)
        dict={
            'data_student' : data_student,
            'desc' : data_course.description
        }

        return render (request , "search_by_student.html", dict)
    else:
        return render (request , "search_by_student.html")
    
    
def search_by_course(request):
    c_code = Course.objects.all()
    if request.method == 'GET' :
        stud_course = Student.objects.filter(course_code = request.GET.get('code'))
        dict = {
            'stud_list' : stud_course,
            'course' : request.GET.get('code'),
            'c_code' : c_code
        }
    else:
        dict = {
            'c_code':c_code
        }
    return render(request,'search_by_course.html',dict)

