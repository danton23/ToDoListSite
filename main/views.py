from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList, UserForm

def index(request,id):
          ls=ToDoList.objects.get(id=id)
          items=ls.item_set.all()
     #ls=ToDoList.objects.all()

          if request.method=="POST":  #note changed all response to request if not work change back!
               print(request.POST)
               if request.POST.get("Start"):
                     form=UserForm(request.POST,request.FILES,instance=ls)
                     if form.is_valid():
                          
                          print("form saved")
                         
                          form.save()
                          
                          
                          return render(request, "main/list.html",{"ls":ls, "items":items, "form":form})

                                    
               elif request.POST.get("save"):
                         for item in ls.item_set.all():
                              if request.POST.get("c"+str(item.id)) =="clicked":
                                   item.complete=True
                                   
                              else:
                                   item.complete=False
                              item.save()     
                                   
                              

               elif request.POST.get("newItem"):
                         txt=request.POST.get("new")
                         if len(txt) >2:
                              ls.item_set.create(text=txt, complete=False)
                         else:
                              print("invalid")
               
               
                          
               
           

         

          return render(request, "main/list.html",{"ls":ls, "items":items, "id":id})

def change(request,id):
          ls=ToDoList.objects.get(id=id)
          items=ls.item_set.all()
     #ls=ToDoList.objects.all()

     
          form=UserForm(request.POST,request.FILES,instance=ls)
          if request.method=="POST":
               #form=UserForm(request.POST,request.FILES,instance=ls)
               
               
               if form.is_valid():
                    form.save()
                    return redirect('success')
               else:
                    form=UserForm(request.POST,request.FILES,instance=ls)
                    
               
           

         

          return render(request, "main/change.html",{"ls":ls, "items":items, "form":form})
def success(request):
               return HttpResponse('successfull uploaded')
        
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
def view(response):
     #try:
               ident=ToDoList.objects.latest('id').id
                  
               ls=ToDoList.objects.get(id=ident)
               items=ls.item_set.all()
               #ls=ToDoList.objects.all()
               if response.method=="POST":
                    print(response.POST)
                    if response.POST.get("save"):
                         for item in ls.item_set.all():
                              if response.POST.get("c"+str(item.id)) =="clicked":
                                   item.complete=True
                                   
                              else:
                                   item.complete=False
                              item.save()     
                                   
                              

                    elif response.POST.get("newItem"):
                         txt=response.POST.get("new")
                         if len(txt) >2:
                              ls.item_set.create(text=txt, complete=False)
                         else:
                              print("invalid")               
               return render(response, "main/list.html",{"ls":ls, "items":items})
     #except:
        #  print("not worked")
         # create(response)
          
def home(response):
     ls=ToDoList.objects.all()
     return render(response, "main/home.html",{"ls":ls})


                
