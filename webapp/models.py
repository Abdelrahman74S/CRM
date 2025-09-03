from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Record(models.Model):
    frist_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    phone = models.IntegerField()
    tall = models.IntegerField()
    wedight = models.IntegerField()
    address =  models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.frist_name + " " + self.last_name
    
    class Meta:
     ordering = ['-create_at']