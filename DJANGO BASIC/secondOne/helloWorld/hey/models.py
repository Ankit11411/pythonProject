from django.db import models

# Create your models here.
class ToDoDo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class item(models.Model):
    tododo = models.ForeignKey(ToDoDo,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    boolean = models.BooleanField()

    def __str__(self):
        return self.text
