from django.urls import path
from . import views
app_name = "schedule"
urlpatterns = [
    path('', views.schedule_list, name='list'),
    path('add/', views.add_schedule, name='add'),
    path('detail/<pk>/', views.schedule_detail, name="detail"),
    # path('<int:pk>/', views.schedule_student, name='schedule'),
]