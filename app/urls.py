# accounts/urls.py
from django.urls import path
from .views import *

app_name = 'app'



urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),

]
