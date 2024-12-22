from django.urls import path
from .views import home_view, modules_view, training_view

urlpatterns = [
    path('', home_view, name="home-view"),
    path('modules/', modules_view, name="modules-view"),
    path('training/', training_view, name="training-view"),
]