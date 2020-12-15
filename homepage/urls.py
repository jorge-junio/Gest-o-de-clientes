from django.urls import path
from .views import homepage, my_logout

urlpatterns = [
    path('', homepage, name='homepage'),
    path('logout/', my_logout, name='logout'),
]
