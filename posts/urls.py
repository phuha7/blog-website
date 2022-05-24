from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register"),
    path('homepage', views.homepage, name="homepage"),
    path('logout', views.logout, name="logout"),
    path('blogs', views.blogs, name="blogs"),
    path('<str:username>', views.profile, name="profile"),
    path('<str:username>/<str:id>', views.post, name="post"),
]