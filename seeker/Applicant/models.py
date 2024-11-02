from django.db import models

# Create your models here.
class Candidate_Profile(models.Model ):
          id= models.AutoField(primary_key=True)
          candidate_name=models.CharField(max_length=100,null=True)
          location=models.CharField(max_length=100,null=True)
          age=models.CharField(max_length=100,null=True) 
          qualification=models.CharField(max_length=100,null=True)
          skills=models.CharField(max_length=100,null=True)
          phone=models.CharField(max_length=100,null=True)
          photo=models.ImageField(null=True)
          experiance=models.CharField(max_length=100,null=True)
          date=models.DateField(null=True)
          username=models.CharField(max_length=100,null=True)
          def __str__(self):
                    return str(self. candidate_name)  
class Apply_Job(models.Model):
            id= models.AutoField(primary_key=True) 
            job_code =models.CharField(max_length=100,null=True)
            candidate_name=models.CharField(max_length=100,null=True)
            job_name=models.CharField(max_length=100,null=True)
            location=models.CharField(max_length=100,null=True)
            age=models.CharField(max_length=100,null=True) 
            qualification=models.CharField(max_length=100,null=True)
            skills=models.CharField(max_length=100,null=True)
            description=models.TextField(max_length=1000,null=True)
            experience=models.CharField(max_length=100,null=True) 
            expect_salary=models.CharField(max_length=100,null=True)
            current_salary=models.CharField(max_length=100,null=True)
            cv_file=models.FileField(null=True)
            status=models.CharField(max_length=100,default="Applied")
            date=models.DateField(null=True)
            photo=models.ImageField(upload_to='images/', default=None)
         
            def __str__(self):
                    return str(self. candidate_name)  
                    