from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm,UserRegisterForm
# Create your views here.
def index(request):
    task_list = Task.objects.all()
    if request.method =='POST':
        name = request.POST .get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)

        task = Task(name=name,priority=priority)
        task.save()
        return redirect('/')

    return render(request,'myapp/index.html',{'task_list':task_list})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)

    if request.method=="POST":
        task.delete()
        return redirect('/')

    return render(request,'myapp/delete.html',{'task':task})


def update(request,id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'task':task})
def register(request):
    if request.method=='POST':
        user_reg_form=UserRegisterForm(request.POST)
        if user_reg_form.is_valid():
            new_user=user_reg_form.save(commit=False)
            new_user.set_password(user_reg_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/register_done.html',{'user_reg_form':user_reg_form})
    else:
        user_reg_form=UserRegisterForm()
    return render (request,'registration/register.html',
                   {'user_reg_form':user_reg_form})
def mark_as_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')
