from django.shortcuts import render
from . models import Tasks


# Create your views here.

def home(request):
    all_data = Tasks.objects.all()
    context = {
        "all_data": all_data
    }
    return render(request, "to_do_list/home.html", context)
