from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add_new_task/", views.create_new_task, name="add_new_task"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
    path("change_task/<int:pk>/", views.change_task, name="change_task"),
    path("mark_task/<int:pk>/", views.mark_task, name="mark_task")


]
