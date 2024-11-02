from django.shortcuts import render,redirect,HttpResponse
from Recruter.models import Compnay_Profile,Add_Jobs
from Applicant.models import Candidate_Profile
from .models import Signup_User
from django.views.generic import View,TemplateView,FormView
from django.utils.timezone import localdate
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from django.contrib.sessions.models import Session
# Create your views here.
class Usergetview(View):
     def get(self,request):
             return render(request,"Userget.html") 
     def post(self,request) :
        userrrole=request.POST.get("userrole")
        if(userrrole == "Employer"):
                return redirect("employer-signup")
        elif(userrrole == "Candidate"):
                   return redirect("candidate-signup")                           
              
class EmployerSignupView(View):
        def get(self,request) :
             return render(request,"Employer-Signup.html")                          
        def post(self,request):
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
          
          
          
          print("name is",name)
          today = localdate()
          obj=Signup_User(
                name=name,
                 location=location,
                 phone=phone,
                 userr_role=userrrole,
                 username=username,
                 password=password,
                 date=today
                 
             )
          obj.save()
         
          obj2=Compnay_Profile(
                        company_name=name,
                        location=location,
                        branchs=branchs,
                        type=type,
                        employes_count=employes_count,
                        website= website,
                        date=date,
                        username=username               
                )
          obj2.save()
                    
          
          return redirect("login")
class CandidateSignupView(View):
        def get(self,request) :
             return render(request,"Candidate-Signup.html")                          
        def post(self,request):
          name=request.POST.get("candidate_name")
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
          
          candidatename=request.POST.get("candidate_name")
          skills=request.POST.get("skills")
          experience=request.POST.get("experiance")
          qualification=request.POST.get("qualification")
          photo=request.FILES['photo'] 
          age=request.POST.get("age")
          
          print("name is",name)
          today = localdate()
          obj=Signup_User(
                name=name,
                 location=location,
                 phone=phone,
                 userr_role=userrrole,
                 username=username,
                 password=password,
                 date=today
                 
             )
          obj.save()
          
         
         
          obj3=Candidate_Profile(
                        candidate_name=candidatename,
                        location=location,
                        skills=skills,
                        experiance=experience,
                        qualification=qualification,
                        age= age,
                        phone=phone,
                        photo=photo,
                        date=date ,
                        username=username        
                    )                       
          obj3.save()
          return redirect("login")

  

class Loginview(View):
        def get(self,request):
                if 'loggedinuser' in request.session:
                        session_uname=request.session.get('loggedinuser')
                        my_string = ' '.join([str(element) for element in session_uname])
                       
                        s_obj=Signup_User.objects.filter(username=my_string).values()
                        print(s_obj[0]['userr_role'])
                        companyname_var=s_obj[0]['userr_role']
                        if(companyname_var == 'Employer'):
                                return redirect("employer_jobs")                   
                        elif(companyname_var == 'Candidate'):                            
                                return redirect("list-jobs-candidate")  
                else:                           
                  return render(request,"Login.html") 
        def post(self,request):
                # Session.objects.all().delete()
                if 'loggedinuser' in request.session:
                        session_uname=request.session.get('loggedinuser')
                        my_string = ' '.join([str(element) for element in session_uname])
                       
                        s_obj=Signup_User.objects.filter(username=my_string).values()
                        print(s_obj[0]['userr_role'])
                        companyname_var=s_obj[0]['userr_role']
                        if(companyname_var == 'Employer'):
                                return redirect("employer_jobs")                   
                        elif(companyname_var == 'Candidate'):                            
                                return redirect("list-jobs-candidate")       
                else:                      
                        uname=request.POST.get("username")
                        passw= request.POST.get("password") 
                        urole= request.POST.get("userrole")
                        obj=Signup_User.objects.filter(username=uname).values()
                        loggedinuser=request.session.get('loggedinuser',[])
                        loggedinuser.insert(0,uname)
                        request.session['loggedinuser']=loggedinuser
                        # print('0000',loggedinguser)
                        # print(obj[0]['name'])
                       
                        # request.session['loggedinpass']=passw
                        
                        # print('tttt',passw)
                        if obj:
                                                
                          if obj[0]['password'] == passw:
                                            
                             if obj[0]['userr_role'] == "Employer":
                                return redirect("employer_jobs")
                             elif obj[0]['userr_role'] == "Candidate":
                                return redirect("list-jobs-candidate")                   
                          else:
                             return  HttpResponse("Incorrect Password")                        
                        else:
                          return  HttpResponse("USER DOES NOT EXIST") 
                                                        
class Employerhomeview(TemplateView):
           template_name = "List_job.html"  
class Candidatehomeview(TemplateView):
           template_name = "Candidate-Home.html"  
           
def signout_view(request):
        del request.session['loggedinuser']
        # request.session.flush() #this command will clear all session data 
        # session_password=request.session.get('loggedinpass')
        # print( "iii",session_password)
        return redirect("login") 
                                    
# def signout_view(request,*args,**kwargs):
                            
#         session_uname=request.session.get('loggedinuser')
        
#         print("hhh",session_uname)
#         logout(request)
#         return redirect("login")
# ................................................................
