from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/watchlist', views.Watchlist.as_view(), name='watchlist'),
    path('accounts/profile', views.Profile.as_view(), name='profile'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
]