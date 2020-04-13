from django.urls import path
from . import views
app_name = "schedule"
urlpatterns = [
    path('', views.schedule_list, name='list'),
    path('<int:pk>/', views.schedule_student, name='schedule'),
]