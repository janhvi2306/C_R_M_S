from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views 
from hello import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
   path("",views.index,name='index'),
   path("about",views.about,name='about'),
   path("services",views.services,name='services'),
   path("contact",views.contact,name='contact'),
   path("register",views.register,name='register'),
   path("handlelogin",views.handlelogin,name='handlelogin'),
   path("applynowform/<str:id>/",views.applynowform,name='applynowform'),
   path("logout_user",views.logout_user,name='logout_user'),
   path("stud_dashboard",views.studDashboard,name='stud_dashboard'),
   path('admin/admin_login',views.admin_login,name="admin/admin_login"),
   path('dashboard',views.dashboard, name="dashboard"),
   path("admin/admin_manageStud/adminstud_det",views.adminstud_det,name="admin/admin_manageStud/adminstud_det"),
   path("admin_header",views.admin_header,name="admin_header"),
   path("admin/admin_manageStud/admin_updateStud/<str:id>/",views.adminUpdateStud,name="admin/admin_manageStud/admin_updateStud"),
   path("admin/admin_manageStud/admin_addrecord",views.adminAddStud,name="admin/admin_manageStud/admin_addrecord"),
   path("admin_deleteStudRecord/<str:id>/",views.deleteStudRecord,name="admin/admin_manageStud/admin_deleteStudRecord"),
   path("admin/admin_manageComp/admincompany_det",views.adminComp_det,name="admin/admin_manageComp/admincompany_det"),
   path("admin/admin_manageComp/adminUpdateComp/<str:id>/",views.adminUpdateComp,name="admin/admin_manageComp/adminUpdateComp"),
   path("admin/admin_manageComp/adminAddComp/",views.adminAddComp,name="admin/admin_manageComp/adminAddComp"),
   path("admin/admin_manageComp/adminRemoveComp/<str:id>/",views.deleteCompRecord,name="admin/admin_manageComp/adminRemoveComp"),
   path("admin_logout",views.admin_logout,name='admin_logout'),
   path("admin/admin_manageStud/appliedcandidates",views.appliedcandidates,name='admin/admin_manageStud/appliedcandidates'),
   path("admin/admin_manageStud/suretoselectcand/<str:id>/",views.select_cand,name='admin/admin_manageStud/suretoselectcand'),
   path("admin/admin_manageStud/shortlistedCand",views.shortlisted_cand,name='admin/admin_manageStud/shortlistedCand'),
   path("admin/admin_manageStud/admin_deleteShortlistedCand/<str:id>/",views.del_shortlistedCand,name='admin/admin_manageStud/admin_deleteShortlistedCand'),
   path("admin/admin_manageStud/suretoremove_appCand/<str:id>/",views.reject_cand,name='admin/admin_manageStud/suretoremove_appCand'),
   # path("jobdet",views.jobs,name='Job_det')
   #path("admin/sendMailToComp",views.send_mail_tocomp,name='admin/sendMailToComp'),
   
   #password reset
  path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
  path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
  path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
  path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),    
   
]
