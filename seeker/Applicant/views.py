from django.shortcuts import render,redirect,HttpResponse
from .models import Candidate_Profile,Apply_Job
from Recruter.models import Add_Jobs
from Login.models import Signup_User
from django.views.generic import View,TemplateView,FormView,CreateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.template import loader
# Create your views here.
# class Add_Candidate_Profileview(CreateView):
#       model=Candidate_Profile
#       fields="__all__"
#       template_name="Add-candprofile.html"
      
#       success_url= reverse_lazy("candidate-home")
class Add_Candidate_Profileview(UpdateView):
      model=Candidate_Profile
      fields="__all__"
      template_name="Edit-Candidateprofile.html"
      pk_url_kwarg="id" 
      context_object_name="jobs" 
      success_url= reverse_lazy("candidate-home")  
      
class Candidate_Profileview(View):
          def get(self,request):
            loggedin_user=request.session.get('loggedinuser')
            my_string = ' '.join([str(element) for element in  loggedin_user])
            user_details=Candidate_Profile.objects.filter(username=my_string).values()
            print(user_details[0]['candidate_name'])
            return render(request,"Add-candprofile.html",{"job":user_details,"username":my_string}) 
      
def updateprofile(request, id):
      obj =Candidate_Profile.objects.get(id=id)
      obj_data = loader.get_template('Edit-Candidateprofile.html')
      context = {
         'jobs': obj,
      }
      
      if request.method =="POST":
            candidatename=request.POST.get("candidate_name")
            skills=request.POST.get("skills")
            experience=request.POST.get("experiance")
            qualification=request.POST.get("qualification")
            location=request.POST.get("location")
            phone=request.POST.get("phone")
            date=request.POST.get("date")
            photo=request.FILES['photo'] 
            age=request.POST.get("age")  
                                 
            obj.age=age
            obj.candidate_name=candidatename
            obj.location=location
            obj.qualification=qualification
            obj.skills=skills
            obj.phone=phone
            obj.date=date
            obj.photo=photo
            obj.experiance=experience
            obj.save()
            return redirect("list-jobs-candidate")
      return render(request,"Edit-Candidateprofile.html",context)
           
           
                                      
           
           
               
                               
       
# class List_Job_View(ListView):
#       model=  Add_Jobs
#       template_name="cand-home.html"
#       context_object_name="alljobs"
class List_Job_View(View):
      def get(self,request):
            loggedin_user=request.session.get('loggedinuser')
            my_string = ' '.join([str(element) for element in  loggedin_user])
            user_details=Signup_User.objects.filter(username=my_string).values()
           
            user_name=user_details[0]['name']
            print("user_name", user_name)
            cand_profile=Apply_Job.objects.filter(candidate_name=user_name).filter(status="Applied").values('job_code','date')
           
            query_length= len(cand_profile)
            print("ttt", cand_profile)
          
            t = []
                
            for course in cand_profile:
                  
                  k= course['job_code']
                  
                  t.append(k)
                  print("3333",k)
                  
            

            jobobj=Add_Jobs.objects.exclude(job_code__in=t)
            print("uuu",jobobj)   
            return render(request,"cand-home.html",{"alljobs":jobobj,"username":my_string}) 
           
      
      
            
            
                                 
      
class Applyjob_view(View):
      def get(self,request,job_code):
           loggedin_user=request.session.get('loggedinuser')
           my_string = ' '.join([str(element) for element in  loggedin_user])
           print(job_code)  
           obj=Add_Jobs.objects.filter(job_code = job_code).values() 
           job_name=obj[0]['job_name']
           obj2=Add_Jobs.objects.filter(job_code = job_code).values('description','expirance')
           print(obj2)
           for course in obj2:
                                      
                  k= course['description']
                  m=course['expirance'] 
           print( m)               
           return render(request,"Apply-job.html",{"job_name": job_name,"job_code":job_code,"username":my_string,"des":k,"exp":m})

      def post(self,request,job_code):
                                
            name=request.POST.get("candidate_name")
            location=request.POST.get("location")
            age=request.POST.get("age")
            qualification=request.POST.get("qualification")
            skills=request.POST.get("skills")
            job_name=request.POST.get("job_name")
            job_code=request.POST.get("job_code")
            expect_salary=request.POST.get("expect_salary")
            current_salary=request.POST.get("current_salary")
            cv_file=request.POST.get("cv_file") 
            desc=request.POST.get("description")
            exp=request.POST.get("exp")
            # photo=request.POST.get("photo",request.FILES)
            photo=request.FILES['photo'] 
            status=request.POST.get("status")                  
            date=request.POST.get("date")
          
            detail=Add_Jobs.objects.get(job_code=job_code)
            # count=detail[0]['application_count']
            count=detail.application_count
            print("ci",count)
            c=int(count)
            obj=Apply_Job(
                 candidate_name=name,
                 job_name= job_name ,
                 location=location,
                 age=age,
                 qualification=qualification,
                 skills=skills,
            #      experiance=experiance,
                 job_code=job_code,
                 expect_salary=expect_salary,
                 current_salary=current_salary,
                 cv_file=cv_file,
                 photo=photo,
                 description=desc,
                 experience=exp,
                 status= "Applied",
                 date= date
            )
            obj.save()
            increment_var=int(c+1)
            count_increment=Add_Jobs.objects.filter(job_code=job_code).update(application_count= increment_var)
            return redirect("list-jobs-candidate")
            
class Myjobsview(View):
        def get(self,request):
            loggedin_user=request.session.get('loggedinuser')
            my_string = ' '.join([str(element) for element in  loggedin_user]) 
            details=Signup_User.objects.filter(username=my_string).values()
            b = details[0]['name']                     
            cand_profile=Apply_Job.objects.filter(candidate_name= b).values()
            return render(request,"My-jobs.html",{"obj":cand_profile,"username":my_string})                               
def Myjob_filterview(request):
      if request.method == 'POST':
            name = request.POST.get('name')
            print("name",name)
            location = request.POST.get('location')
            date=request.POST.get('date')
            print(date)
            loggedin_user=request.session.get('loggedinuser')
            my_string = ' '.join([str(element) for element in  loggedin_user]) 
      try:      
            if(name!=""and location !="" and date!=""):
                  obj=Apply_Job.objects.filter(job_name=name).filter(location=location).filter(date=date)
                  if(obj[0] == []):
                                                      
                     obj="No Data Found"   
            elif(location =="" and date ==""):  
                  obj=Apply_Job.objects.filter(job_name=name)
                  if(obj[0] == []):
                                                      
                     obj="No Data Found"   
            elif(name=="" and date ==""):  
                  obj=Apply_Job.objects.filter(location=location)
                  if(obj[0] == []):
                                                      
                     obj="No Data Found"   
            elif( date ==""):  
                  obj=Apply_Job.objects.filter(job_name=name,location=location)
                  if(obj[0] == []):
                                  
                     obj="No Data Found"   
            elif( name =="" and location ==""):  
                  obj=Apply_Job.objects.filter(date=date)
                  print("jj") 
                  if(obj[0] == []):
                     print("jj")                       
                     obj="No Data Found"  
            elif(obj[0] == []):
                  obj="No Data Found"                            
           
              
      except:
            obj="No Data Found"      
      print(obj)    
      return render(request,"My-jobs.html",{"obj":obj,"username": my_string})                                         
            
def filterjobview(request):
      if request.method == 'POST':
            name = request.POST.get('name')
            print("name",name)
            location = request.POST.get('location')
            exp=request.POST.get('exp')
      if(name!=""and location !="" and exp!=""):
              obj=Add_Jobs.objects.filter(job_name=name).filter(location=location).filter(expirance=exp)
      elif(location =="" and exp ==""):  
              obj=Add_Jobs.objects.filter(job_name=name)
      elif(name=="" and exp ==""):                          
               obj=Add_Jobs.objects.filter(location=location)
               
      print(obj)   
          
      return render(request,"cand-home.html",{"alljobs":obj})                                                                                          