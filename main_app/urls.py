from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('movie/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('profile/<int:pk>/watchlist', views.Watchlist.as_view(), name='watchlist'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
]