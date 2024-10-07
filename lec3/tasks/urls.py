from django.urls import path
from . import views
app_name = "tasks"
urlpatterns = [
        path("", views.show, name = 'show'),
        path("add/", views.add, name = 'add')
        ]
