from django.shortcuts import render,get_object_or_404,redirect
from .forms import Studentform
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request,'Students/student_list.html',{'Students':students})

def create_student(request):
    if request.method=='POST':
        form = Studentform(request.POST)
        form.is_valid()
        form.save()
        return redirect('student_list')
    else:
            form = Studentform()
            return render(request,'Students/create_student.html',{'form':form})


def delete_Student(request,studentid):
    student = get_object_or_404(Student,studentid=studentid)
    student.delete()
    return redirect('student_list')