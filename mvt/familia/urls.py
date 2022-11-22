from django.urls import path
from familia.views import *

urlpatterns = [
    path('',inicio),
    path('papa/',mipapa),
    path('mama/',mimama),
    path('hermano/',mihermano)
]
