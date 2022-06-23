from unicodedata import name
from django.db import models

# Create your models here.

class HomePage(models.Model):
    img1 = models.ImageField('HomePage img1',upload_to='media')
    img2 = models.ImageField('HomePage img2',upload_to='media')
    img3 = models.ImageField('HomePage img3',upload_to='media')
    name1 = models.CharField('HomePage name1', max_length=50)
    name2 = models.CharField('HomePage name2', max_length=60)
    name3 = models.CharField('HomePage name3', max_length=70)
    about = models.TextField('HomePage about')
    number = models.CharField('HomePage number', max_length=30)

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'




class AboutPage(models.Model):
    name1 = models.CharField('AboutPage name1', max_length=50)
    about1 = models.TextField('AboutPage about1')
    about2 = models.TextField('HomePage about2')
    year = models.IntegerField('AboutPage year')
    name2 = models.CharField('AboutPage name2', max_length=60)
    name3 = models.CharField('AboutPage name3', max_length=70)
    img1 = models.ImageField('AboutPage img1',upload_to='media')
    img2 = models.ImageField('AboutPage img2',upload_to='media')
   

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'




class TimelinePage(models.Model):
    name = models.CharField('TimelinePage name', max_length=50)
    about = models.TextField('TimelinePage about')
    year = models.CharField('TimelinePage year', max_length=30)
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Timeline'
        verbose_name_plural = 'Timelines'


class TestPage(models.Model):
    title = models.CharField('TestPage title', max_length=50)
    about = models.TextField('TestPage about')
    name = models.TextField('TestPage name')
    surname = models.TextField('TestPage surname')
    img = models.ImageField('TestPage img1',upload_to='media', null=True)

   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'