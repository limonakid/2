from django.contrib import admin
from django.urls import path
from planner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create_event, name='create_event'),
    path('events/', views.events_list, name='events_list'),
]
