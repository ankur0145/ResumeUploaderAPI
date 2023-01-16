from django.urls import path
from API import views

urlpatterns = [
    path('resume/',views.ProfileView.as_view(),name='resume'),
    path('list/',views.ProfileView.as_view(),name='list')

]