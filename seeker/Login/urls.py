from django.urls import path
from Login import views
urlpatterns = [
   path("userget/",views.Usergetview.as_view(),name="userget"),
  path("employer-signup/",views.EmployerSignupView.as_view(),name="employer-signup"),
  path("candidate-signup/",views.CandidateSignupView.as_view(),name="candidate-signup"),

  path("",views.Loginview.as_view(),name="login") , 
  # path("employer/",views.Employerhomeview.as_view(),name="employer-home") , 
  path("candidate/",views.Candidatehomeview.as_view(),name="candidate-home") , 
   path("signout",views.signout_view,name="signout") ,
]
