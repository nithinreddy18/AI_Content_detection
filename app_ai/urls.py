from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='main'),           # main.html
    path('detect/', views.detect_view, name='detect'),   # feature.html
    path('about/', views.about_team, name='about'),      # about.html
]
