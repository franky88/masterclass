from django.urls import path
from . import views
app_name = "section"
urlpatterns = [
    path('', views.section_list, name='list'),
]