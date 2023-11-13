from django.urls import path
from . import views


urlpatterns = [
    path("home/",views.home, name="home"),
    path("add_new_task/",views.create_new_task,name="add_new_task"),
]