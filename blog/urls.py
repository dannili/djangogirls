from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # assign post_list view to the root URL
]