from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



class newForm(forms.Form):
    task = forms.CharField(label="New Task")

def show(request):
    #del(request.session["tasks"])
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request ,"tasks/index.html", {"tasks": request.session["tasks"]})


def add(request):
    if request.method == "POST":
        form = newForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            taskslist = request.session["tasks"]
            taskslist.append(task)
            request.session["tasks"] = taskslist
            print(type(request.session["tasks"]))

            return HttpResponseRedirect(reverse("tasks:show"))
        else:
            return render(request, "tasks/add.html", {"form": form})

    return render(request ,"tasks/add.html", {"form": newForm()})
