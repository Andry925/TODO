from django.shortcuts import render,redirect
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

