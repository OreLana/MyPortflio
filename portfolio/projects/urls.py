from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path("project/", views.project_index, name="project_index"),
    path("about/", views.about_index, name="about_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]