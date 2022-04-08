from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            student = form.save()
            return redirect('classroom:detail', student.pk)
    
    elif request.method == 'GET':
        form = StudentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'classroom/create.html', context)



def index(request):
    classroom = Student.objects.order_by('-pk')
    context = {
        'classroom' : classroom,
    }
    return render(request, 'classroom/index.html', context)


def detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {
        'student' : student,
    }
    return render(request, 'classroom/detail.html', context)


def delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('classroom:index')
    else:
        return redirect('classroom:detail', student.pk)

# def edit(request, pk):
#     pass
def update(request, pk):
    pass

