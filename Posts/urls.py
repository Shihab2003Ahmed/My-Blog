from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path("category/<str:category>/", views.category_posts, name="category_posts"),
   
]
