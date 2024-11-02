from django.db import models

# Create your models here.
class Compnay_Profile(models.Model ):
          id= models.AutoField(primary_key=True)
          company_name=models.CharField(max_length=100,null=True)
          location=models.CharField(max_length=100,null=True)
          branchs=models.CharField(max_length=100,null=True) 
          type=models.CharField(max_length=100,null=True)
          employes_count=models.CharField(max_length=100,null=True)
          website=models.CharField(max_length=100,null=True)
          date=models.DateField(null=True)
          username=models.CharField(max_length=100,null=True)
          def __str__(self):
                    return str(self. company_name)  
class Add_Jobs(models.Model ):
          id= models.AutoField(primary_key=True)
          job_name=models.CharField(max_length=100,null=True)
          company_name=models.CharField(max_length=100,null=True)
          location=models.CharField(max_length=100,null=True)
          expirance=models.CharField(max_length=100,null=True) 
          salary=models.CharField(max_length=100,null=True)
          qualification=models.CharField(max_length=100,null=True)
          description=models.TextField(max_length=1000,null=True)
          application_count=models.CharField(max_length=100,default=0)
          job_code =models.CharField(max_length=100,null=True,unique=True)
          skills=models.CharField(max_length=100,null=True)
          age=models.CharField(max_length=100,null=True) 
          
          date=models.DateField(null=True)
          def __str__(self):
                    return str(self. job_name)  