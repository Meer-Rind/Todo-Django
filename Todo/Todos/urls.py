from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.Register_view,name='register'),
    path('login/',views.Login_view,name='login'),
    path('Task_list',views.Task_list,name='Task_list'),
    path('add_task/',views.add_task, name="add_task"),
    path('edit_task/<int:task_id>/',views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/',views.delete,name='delete')
]
