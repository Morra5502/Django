from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.home, name="login"),
    path('register/', views.home, name="register"),
    path('logout/', views.home, name="logout"),
    path('organizer/', views.organizer_dashboard, name="organizer_dashboard"),
    path('participant/', views.participant_dashboard, name="participant_dashboard"),
    path('add_event/', views.home, name="add_event"),
    path('manage_participants/', views.home, name="manage_participants"),
    path('publish_results/', views.home, name="publish_results"),
    path('browse_events/', views.home, name="browse_events"),
    path('my_registrations/', views.home, name="my_registrations"),
    path('my_results/', views.home, name="my_results"),
]