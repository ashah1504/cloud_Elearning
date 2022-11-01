from . import views
from django.urls import path

urlpatterns = [
    path('projects/', views.projects, name='proj' ),
    path('new_project', views.NewProject, name='NewProj' ),
    path('Delete_project/<int:id>/', views.DelProject, name='DelProj' ),
    path('Update_project/<int:id>/', views.UpProject, name='UpProj' ),
    
    path("events_signup/", views.events_signup, name="event_signup"),
]
