from django.urls import url
from . import views


urlpatterns = [
    path('', views.users , name='users'),
]