from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'), 
    path('text/', include('textprocessor.urls')), 
    path('pesel/', include('peselApp.urls'))
]
