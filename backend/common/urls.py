from django.urls import path

from . import views

app_name = 'common'
urlpatterns = [
    path('healthcheck', views.health_check),
]