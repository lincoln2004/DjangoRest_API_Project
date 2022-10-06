from django.db import models

# Create your models here.


class vegetals(models.Model):
    
    name = models.CharField(max_length=80)
    stock = models.IntegerField()
    validity = models.DateField()
    
    def __str__(self) -> str:
        return f' [ name: {self.name}; stock: {self.stock}; validity: {self.validity}  ]'
    
    
class fruits(models.Model):
    
    name = models.CharField(max_length=80)
    stock = models.IntegerField()
    validity = models.DateField()
    
    def __str__(self) -> str:
        return f' [ name: {self.name}; stock: {self.stock}; validity: {self.validity}  ]'  
    
    
