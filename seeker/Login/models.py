from django.db import models

# Create your models here.
class Signup_User(models.Model ):
          id= models.AutoField(primary_key=True)
          name=models.CharField(max_length=100,null=True)
          location=models.CharField(max_length=100,null=True)
          phone=models.CharField(max_length=100,null=True) 
         
          userr_role=models.CharField(max_length=100,null=True)
          username=models.CharField(max_length=100,unique=True,null=True)
          password=models.CharField(max_length=100,null=True)
          date=models.DateField(null=True)
          def __str__(self):
                    return str(self. name)


        