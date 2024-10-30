from django.urls import path
from .import views

urlpatterns = [
  
     
     path('', views.entry, name = 'entry'),
     path('newpatient', views.newpatient, name = 'newpatient'),
     path('patiententrypage', views.patiententrypage, name = 'patiententrypage'),
     path('loginpatient', views.loginpatient, name = 'loginpatient'),
     path('patientedit', views.patientedit, name = 'patientedit'),
     path('patiententrynew', views.patiententrynew, name = 'patiententrynew'),
     path('delete/<int:user_id>/', views.delete, name='delete'),
     path('edit/<int:user_id>/',views.edit,name='edit'),
     path('update/<int:pk>',views.update,name='update'),
     path('ptnsignout', views.ptnsignout, name='ptnsignout'),
     path('changepassptn', views.changepassptn, name='changepassptn'),
     path('logindoctor', views.logindoctor, name='logindoctor'),
     path('newdoctor', views.newdoctor, name='newdoctor'),
     path('doctoredit', views.doctoredit, name='doctoredit'),
     path('drsignout', views.drsignout, name='drsignout'),
     path('drchangepass', views.drchangepass, name='drchangepass'),
     path('druploadpres', views.druploadpres, name='druploadpres'),
     path('viewpatientdetails', views.viewpatientdetails, name='viewpatientdetails'),
     path('viewptnupdetails', views.viewptnupdetails, name='viewptnupdetails'),
     path('viewdrupdetails', views.viewdrupdetails, name='viewdrupdetails'),
      path('newadmin', views.newadmin, name='newadmin'),
     path('adminpage', views.adminpage, name='adminpage'),
     path('adminlogin', views.adminlogin, name='adminlogin'),
     path('newadmin', views.newadmin, name='newadmin'),
     path('adminviews', views.adminviews, name='adminviews'),
     path('deletedr/<int:user_id>/', views.deletedr, name='deletedr'),
     # path('save/',views.save,name='save'),
     path('loginptnfpres', views.loginptnfpres, name='loginptnfpres'),
     path('viewpresptn', views.viewpresptn, name='viewpresptn'),
     path('drloginvptn', views.drloginvptn, name='drloginvptn'),
     
     
     
  
   



]