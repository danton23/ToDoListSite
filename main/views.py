from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList, UserForm

def index(request,id):
          allls=ToDoList.objects.all()
          largest=ToDoList.objects.latest('id').id
          print(largest)
          latest=ToDoList.objects.get(id=largest)
          print(latest.id)
          print(latest.name)
          
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
                          
                          
                          return render(request, "main/list.html",{"ls":ls, "items":items, "form":form, "allls":allls,"latest":latest})

               
               elif request.POST.get("save"):
                                 print("save seleced")
                                 for item in ls.item_set.all():
                                      if request.POST.get("d"+str(item.id))=="delete":
                                          print(len(ls.item_set.all()))
                                          no_items=len(ls.item_set.all())
                                          """if no_items==1:
                                              print("LAST ITEM")
                                              items.filter(id=item.id).delete()
                                              for item in items:
                                                  item.save()
                                                  print("saved")
                                              ls.delete()
                                              print("ls update")
                                              pass"""
                                          print("Entered Here")
                                          print(str(item.text)+"delete selected")
                                          items=ls.item_set.all()
                                          items.filter(id=item.id).delete()
                                          for item in items:
                                              item.save()
                                          """if no_items==1:
                                              ls.item_set.all().pop[0]"""
                                          print(items)
                                          items=ls.item_set.all()
                                          
                                          print(items)
                                          
                                          pass
                                          
                                      else:
                                          if request.POST.get("c"+str(item.id)) =="clicked":
                                              item.complete=True
                                              item.save()
                                           
                                          else:
                                             item.complete=False
                                             item.save()                        
               
                                   
                              

               elif request.POST.get("newItem"):
                         txt=request.POST.get("new")
                         if len(txt) >2:
                              ls.item_set.create(text=txt, complete=False)
                         else:
                              print("invalid")
               
               
                          
               
                   

         

          return render(request, "main/list.html",{"ls":ls, "items":items, "id":id, "allls":allls,"latest":latest})

def test(request):
     nums=[1,2,3]
    
     return render(request, "main/test.html",{"nums":nums,"range":range(10)})

def change(request,id):
          ls=ToDoList.objects.get(id=id)
          items=ls.item_set.all()
          oldname=ls.name
     #ls=ToDoList.objects.all()

     
          form=UserForm(request.POST,request.FILES,instance=ls)
          if request.method=="POST":
               #form=UserForm(request.POST,request.FILES,instance=ls)
               
               
               if form.is_valid():
               
                    if form.cleaned_data.get('name') == None:
                        print("entered")
                         
                        
                        form.save()
                        ls.name=oldname #if no name entered will revert to old one
                        ls.save()
                    else:    
                         form.save()
                    # return redirect('success')
                    return redirect('index',id)
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
               allls=ToDoList.objects.all()
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
               return render(response, "main/list.html",{"ls":ls, "items":items, "allls":allls})
     #except:
        #  print("not worked")
         # create(response)
          
def home(response):
     ls=ToDoList.objects.all()
     return render(response, "main/home.html",{"ls":ls})


                
