
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
