
from django.contrib import admin
from django.urls import path
from map import views as map_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',map_views.index , name='index'),
]
