from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name="add"),
    path('delete<int:taskid>/',views.delete,name="delete"),
    path('update<int:id>/',views.update,name="update"),
    path('listview',views.tasklistview.as_view(),name="listview"),
    path('detailview/<int:pk>/',views.taskdetailview.as_view(),name="detailview"),
    path('updateview/<int:pk>/',views.taskupdateview.as_view(),name="updateview"),
    path('deleteview/<int:pk>/',views.taskdeleteview.as_view(),name="deleteview"),
]
