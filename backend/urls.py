from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("signup/", views.signup),
    path("signin/", views.signin),
    path("task/", views.task),
    path("edit_task/<int:srno>", views.edit_task, name="edit_task"),
    path("delete_task/<int:srno>", views.delete_task),
    path("signout/", views.signout, name="signout")
]
