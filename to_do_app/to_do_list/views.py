from django.shortcuts import render, redirect, get_object_or_404
from . models import Tasks


def home(request):
    all_data = Tasks.objects.all()
    context = {
        "all_data": all_data
    }
    return render(request, "to_do_list/home.html", context)


def create_new_task(request):
    if request.method == "POST":
        declared_task = request.POST["add_a_task"]
        Tasks.objects.create(task=declared_task)
    return redirect("home")


def delete_task(request, pk):
    task_to_delete = get_object_or_404(Tasks, pk=pk)
    task_to_delete.delete()
    return redirect("home")


def change_task(request, pk):
    if request.method == "GET":
        task_to_dispay = get_object_or_404(Tasks, pk=pk)
        context = {
            "task_to_display": task_to_dispay
        }
        return render(request, "to_do_list/edit_task.html", context)
