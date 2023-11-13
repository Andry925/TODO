from django.shortcuts import render,redirect,get_object_or_404
from . models import Tasks



# Create your views here.

def home(request):
    all_data = Tasks.objects.all()
    context = {
        "all_data": all_data
    }
    return render(request, "to_do_list/home.html", context)

def create_new_task(request):
    if request.method == "POST":
        declared_task = request.POST["add_a_task"]
        Tasks.objects.create(task= declared_task)
    return redirect("home")

def delete_task(request,pk):
    get_task = get_object_or_404(Tasks,pk=pk)
    get_task.delete()
    return redirect("home")


