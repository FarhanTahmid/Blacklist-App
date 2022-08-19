from django.db import models

class Users(models.Model):
    userid=models.CharField(max_length=40,null=False,blank=False,verbose_name="Student ID",primary_key=True)
    name=models.CharField(max_length=50,null=False,blank=False,verbose_name="Student Name")
    email=models.EmailField(max_length=50,null=False,blank=False,verbose_name="Email")
    
    def __str__(self):
        return self.userid