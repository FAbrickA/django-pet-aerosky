from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.page_about, name="about"),
    path('services/', views.page_services, name="services"),
    path('price/', views.page_price, name="price"),
    path('projects/', views.page_projects, name="projects"),
    path('contact/', views.page_contact, name="contact"),
    path('right-sidebar/', views.page_right_sidebar, name="right-sidebar"),
]
