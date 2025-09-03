from django.urls import path
from . import views

urlpatterns = [
      path('osduapp/test', views.test, name='test'),
             
      path('osdu/well/get' , views.getallwell , name="getwell"),
      path('osdu/create', views.create_well, name='item_list_create'),
      path('osdu/add', views.addwell, name='item_list_create'),
      path('osdu/delete',views.delete_byid,name='well_delete'),
      path('osdu/GetProduction',views.getProduction,name='well_delete'),
      path('osdu/api/gettypepool' , views.GetPooType , name = "Getpooltype")
 
]
