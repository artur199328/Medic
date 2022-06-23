from django.contrib import admin
from .models import HomePage, AboutPage, TimelinePage, TestPage
# Register your models here.


admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(TimelinePage)
admin.site.register(TestPage)