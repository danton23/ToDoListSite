from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response):
     
     ts=ToDoList.objects.all()
    
     
     
               
               
               
     return render(response, "main/list.html",{"lists":ts})
def home(response):
     return render(response, "main/home.html",{"name":"test"})
def create(response):
            if response.method=="POST":
                 print("goober")
                 form = CreateNewList(response.POST)
                 if form.is_valid():
                           n = form.cleaned_data["name"]
                           t = ToDoList(name=n)
                           t.save()
                           print("saved")
                           #return HttpResponseRedirect("/%i" %t.id)
                           return render(response, "main/create.html",{"form":form}) 
            else:
                form = CreateNewList()
            return render(response, "main/create.html",{"form":form})  

                
