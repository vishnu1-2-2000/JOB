from django.urls import path
from Recruter import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
   path('', views.Navbarview.as_view(),name="navbar" ),
   # path('companyprofile', views.AddCompanyview.as_view(),name="company" ),
   path('companyprofile', views.Company_Profileview.as_view(),name="company" ),
   path("edit-company-profile/<id>",views.update_companyprofile,name="edit-company-profile"),
   
   path('addjob', views.Addjobview.as_view(),name="addjob" ) ,
#    path('listjob', views.JobListview.as_view(),name="employer_jobs" ), 
   path('editjob/<id>', views.Editjobview.as_view(),name="edit_job" ),
   path('deletejob/<id>', views.Deletejobview.as_view(),name="delete_job" ),
    # path('get_company', views.Getcompanyprofile.as_view(),name="get_company" ), 
   path('listjob', views.GetCompanyPro_ListJobview.as_view(),name="employer_jobs" ), 
   path('viewapplication/<job_code>', views.Viewapplication,name="viewapplication" ),
   path('application_status/<id>', views.Respond_Application_View.as_view(),name="application_status" ),
   path('filterjobs',views.filterjob,name='filterjobs')
    
    
]
