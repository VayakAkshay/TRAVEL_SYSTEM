from django.urls import path
from . import views
urlpatterns = [
    path('',views.Homepages,name="Homepages"),
    path('about/',views.Aboutpage,name="Aboutpage"),
    path('events/',views.Eventpage,name="Eventpage"),
    path('team/',views.Teampage,name="Teampage"),
    path('contact/',views.Contactpage,name="Contactpage"),
    path('profile/',views.Profile_page,name="Profile_page"),
    path('event-detail/<id>',views.Event_detail,name="Event_detail"),
    path('edit-profile/',views.edit_profile,name="edit_profile"),
    path('Review-page/',views.Review_page,name="Review_page"),
    path('logout/',views.logout_page,name="logout_page"),
]