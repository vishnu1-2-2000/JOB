from django.urls import path
from Applicant import views
urlpatterns = [ 
  path("view-cadidate-profile/",views.Candidate_Profileview.as_view(),name="view-cadidate-profile"),             
  path("edit-profile/<id>",views.updateprofile,name="edit-profile"),

  path("list-jobs",views.List_Job_View.as_view(),name="list-jobs-candidate"),
  path("apply-jobs/<job_code>/",views.Applyjob_view.as_view(),name="apply-job") ,
  
  path("my-jobs",views.Myjobsview.as_view(),name="my-jobs"),
  path("myjob_filter-job",views.Myjob_filterview,name="my_filter-job"),    

  path("filter-job",views.Myjob_filterview,name="filter-job")    
]
