from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='poll_list'),
    path('<int:id>/details', details, name='poll_details'),
    path('<int:id>', poll, name='single_poll')
]