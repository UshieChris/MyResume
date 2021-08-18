from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('personal', views.personal, name = 'personal')
]