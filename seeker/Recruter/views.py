from django.shortcuts import render,redirect,HttpResponse
from .models import Add_Jobs,Compnay_Profile
from django.views.generic import View,TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from Login.models import Signup_User
from Applicant.models import Apply_Job

# Create your views here.
class Navbarview(View):
       def get(self,request):
             session_uname=request.session.get('loggedinuser')
             my_string = ' '.join([str(element) for element in session_uname]) 
             print("1111111",my_string)                       
             return render(request,"Navbar.html",{"username": my_string})                  
# class AddCompanyview(CreateView):
                   
#         model=Compnay_Profile
#         template_name = "company_profile.html"
#         fields="__all__"
#         success_url = reverse_lazy("employer_jobs")        
class Addjobview(CreateView):
        model =Add_Jobs
        template_name="Addjob.html"
        # fields="__all__"
       
        fields=("job_name","company_name","location","expirance","salary","qualification","description","job_code","skills","age","date")
        
        success_url=reverse_lazy("employer_jobs")
       
# class JobListview(ListView):
#            model = Add_Jobs
#            context_object_name = "jobs"
#            template_name = "List_job.html"  
# class GetCompanyPro_ListJobview(ListView):
#            model = Compnay_Profile
#            context_object_name = "company"
#            template_name = "List_job.html"

class GetCompanyPro_ListJobview(View):
        def get(self,request):
              session_uname=request.session.get('loggedinuser')
              print('0000',session_uname) 
              my_string = ' '.join([str(element) for element in session_uname])
              print("1111",my_string)
              s_obj=Signup_User.objects.filter(username=my_string).values()
              print(s_obj[0]['name'])
              companyname_var=s_obj[0]['name']
              
            
                          
              obj=Add_Jobs.objects.filter(company_name=companyname_var)
              obj2=Compnay_Profile.objects.filter(company_name=companyname_var)
              print("hhjh",obj[0].application_count)
              
            
              return render(request,"List_job.html",{"jobs":obj,"company":obj2,"username":my_string})  
def filterjob(request):
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
                  obj=Add_Jobs.objects.filter(job_name=name).filter(location=location).filter(date=date)
                  if(obj[0] == []):
                                                      
                     obj="No Data Found"   
            elif(location =="" and date ==""):  
                  obj=Add_Jobs.objects.filter(job_name=name)
                  if(obj[0] == []):
                                                      
                     obj="No Data Found"   
            elif(name=="" and date ==""):  
                  obj=Add_Jobs.objects.filter(location=location)
                  if(obj[0] == []):
                                                      
                     obj="No Data Found"   
            elif( date ==""):  
                  obj=Add_Jobs.objects.filter(job_name=name,location=location)
                  if(obj[0] == []):
                                  
                     obj="No Data Found"   
            elif( name =="" and location ==""):  
                  obj=Add_Jobs.objects.filter(date=date)
                  print("jj") 
                  if(obj[0] == []):
                     print("jj")                       
                     obj="No Data Found"  
            elif(obj[0] == []):
                  obj="No Data Found"                            
           
              
        except:
            obj="No Data Found"      
        print(obj)    
          
        return render(request,"List_job.html",{"jobs":obj})
                                               
                           
class Editjobview(UpdateView):
        model=Add_Jobs
        context_object_name="jobs"
        template_name="Editjob.html"
        fields=("job_name","company_name","location","expirance","salary","qualification","description","skills","age","date")
        # exclude = ("application_count","job_code")
        pk_url_kwarg="id" 
        success_url=reverse_lazy("employer_jobs")
class Deletejobview(View):
        def get(self,request,id):             
                    obj=Add_Jobs.objects.get(id=id)
                    obj.delete()
                    return redirect("employer_jobs")
            
       
def Viewapplication(request,job_code):
       
        obj=Apply_Job.objects.filter(job_code=job_code).values()
        session_uname=request.session.get('loggedinuser')
        u=request.GET.get('subject4')
        print("uu",u)     
        my_string = ' '.join([str(element) for element in session_uname])
        return render(request,"View_applications.html",{"obj":obj,"username":my_string }) 

class Respond_Application_View (View):
        def get(self,request,id):
          
            obj=Apply_Job.objects.filter(id=id).values()
            print(obj[0]['photo'])
            session_uname=request.session.get('loggedinuser')
              
            my_string = ' '.join([str(element) for element in session_uname])
           
           
            status_update_by_get=Apply_Job.objects.filter(id=id).update(status="Viewed")
        #     print(request.GET)
            
            j=request.GET.get('subject')
            print("jjjj",j)
            k=request.GET.get('subject2')
            if j=="ACCEPT":
              status_update_by_button_click=Apply_Job.objects.filter(id=id).update(status="Accepted")
              
            elif k =="REJECT":
                status_update_by_button_click=Apply_Job.objects.filter(id=id).update(status="Rejected")
               
            return render(request,"Status-Application.html",{"obj":obj,"username":my_string})
       
class Company_Profileview(View):
        def get(self,request):
            loggedin_user=request.session.get('loggedinuser')
            my_string = ' '.join([str(element) for element in  loggedin_user])
            user_details=Compnay_Profile.objects.filter(username=my_string).values()
            print(user_details[0]['company_name'])
            return render(request,"company_profile.html",{"job":user_details,"username":my_string}) 
      
def update_companyprofile(request, id):
        obj =Compnay_Profile.objects.get(id=id)
       
        context = {
                'jobs': obj,
        }
      
        if request.method =="POST":
                name=request.POST.get("name")
                location=request.POST.get("location")
                phone=request.POST.get("phone")
                userrrole=request.POST.get("userr_role")
                username=request.POST.get("username")
                password=request.POST.get("password")
                
                branchs=request.POST.get("branchs")
                type=request.POST.get("type")
                employes_count=request.POST.get("employes_count")
                website=request.POST.get("website")
                date=request.POST.get("date")
                                        
                obj.company_name=name
                
                obj.location=location
                obj.branchs=branchs
                obj.employes_count=employes_count
                obj.website=website
                obj.date=date
               
                obj.save()
                return redirect("employer_jobs")
        return render(request,"Edit-Companyprofile.html",context)                                   
                                  

   
                            
                                              