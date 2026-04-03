from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Show all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Add student
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/add_student.html', {'form': form})

# Update student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/update_student.html', {'form': form})

# Delete student

def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})