from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomePage, AboutPage, TimelinePage, TestPage
# Create your views here.


class HomePageListViews(ListView):
    template_name='index.html'

    def get(self,request):
        homes = HomePage.objects.all()
        return render(request,self.template_name,{'homes':homes})



class AboutPageListViews(ListView):
    template_name='about.html'

    def get(self,request):
        abouts = AboutPage.objects.all()
        return render(request,self.template_name,{'abouts':abouts})



class TimelinePageListViews(ListView):
    template_name='timeline.html'

    def get(self,request):
        times = TimelinePage.objects.all()
        return render(request,self.template_name,{'times':times})



class TestPageListViews(ListView):
    template_name='testimonials.html'

    def get(self,request):
        tests = TestPage.objects.all()
        return render(request,self.template_name,{'tests':tests})


def Booking(request):
    return render(request, 'booking.html')