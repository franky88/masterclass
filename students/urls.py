from django.urls import path
from . import views
app_name = "student"
urlpatterns = [
    path('', views.my_list, name='list'),
    path('<int:pk>/details/', views.student_detail, name='detail'),
    path('add/', views.student_add, name='add'),
    path('edit/<int:pk>/', views.student_edit, name='edit'),
    path('update/<int:pk>/', views.student_update, name='update'),
    path('schedule/<int:pk>/', views.schedule_student, name='schedule'),
    path('delete/<int:pk>/', views.delete_student, name='delete'),
]