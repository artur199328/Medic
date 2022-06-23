from django.urls import path
from . import views
from .views import   HomePageListViews, AboutPageListViews, TimelinePageListViews, TestPageListViews

urlpatterns = [
    path('', HomePageListViews.as_view(), name='home'),
    path('about/', AboutPageListViews.as_view(),  name='about'),
    path('timeline/', TimelinePageListViews.as_view(),  name='time'),
    path('testimonials/', TestPageListViews.as_view(),  name='test'),
    path('booking/', views.Booking, name='booking'),

]