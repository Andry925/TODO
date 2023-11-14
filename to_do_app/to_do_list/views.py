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
    task_to_display = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        data_from_form = request.POST["edited_task"]
        task_to_display.task = data_from_form
        task_to_display.save()
        return redirect("home")
    context = {
        "task_to_display": task_to_display
    }
    return render(request, "to_do_list/edit_task.html", context)


def mark_task(request, pk):
    done_task = get_object_or_404(Tasks, pk=pk)
    done_task.task_is_completed = True
    done_task.save()
    return redirect("home")
