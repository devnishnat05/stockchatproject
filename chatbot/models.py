from django.db import models

# Create your models here.
class Books( models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    
    def __str__(self):
        
        return self.name

