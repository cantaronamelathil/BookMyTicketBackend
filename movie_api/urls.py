from django.urls import path
from . import views


urlpatterns = [
    path('',views.TicketBookHomeView.as_view(),name='home'),
    path('<int:id>/',views.SpecificMovieDetails.as_view(),name='moviedetails'),
    
    
]