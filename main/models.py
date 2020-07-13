from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name= models.CharField(max_length=200, null=True, blank=True)
    image= models.ImageField(null=True,blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist=models.ForeignKey(ToDoList, on_delete=models.CASCADE, null=True)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
         return self.text
        
