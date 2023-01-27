from django.db import models

# Create your models here.
#Step 1
class inform(models.Model):
    
    Title= models.CharField(max_length=30)
    Hwidth=models.CharField(max_length=30)
    Price=models.IntegerField()
    Lstatus=models.BooleanField(default=False)