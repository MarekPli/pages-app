from django.urls import path
from .views import DBPageView

urlpatterns = [
    path('db', DBPageView.as_view(), name='db'),
]